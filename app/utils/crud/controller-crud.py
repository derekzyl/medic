from typing import Any, Dict, List, Type

from fastapi import (APIRouter, Depends, HTTPException, Request, Response,
                     status)
from sqlalchemy.orm import Session


class CrudController:
    def __init__(self, model: Type, schema: Type, db: Session):
        self.model = model
        self.schema = schema
        self.db = db
        self.service = CrudService(model, schema, db)

    async def get_many(
        db: Session,
        model: Type[T],
        query: Dict[str, Any],
        filter: Dict[str, Any] = None,
        select: list = None
    ) -> ResponseMessage:
        query_model = db.query(model)
        
        if filter:
            for key, value in filter.items():
                query_model = query_model.filter(getattr(model, key) == value)
        
        query_handler = Queries(query_model, query)
        query_handler.filter().limit_fields().paginate().sort()
        
        results = query_handler.model.all()
        
        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not fetched")
        
        return ResponseMessage(
            success_status=True,
            message="Data fetched successfully",
            data=results,
            doc_length=len(results)
        )

    async def get_one(self, request: Request, response: Response, data: Dict[str, Any], select: List[str] = None, populate: Dict[str, Any] = {}):
        item = self.service.get_one(data, select, populate)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    async def create(self, request: Request, response: Response, data: Dict[str, Any]):
        item = self.service.create(data)
        return item

    async def update(self, request: Request, response: Response, item_id: int, data: Dict[str, Any]):
        item = self.service.update(item_id, data)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    async def delete(self, request: Request, response: Response, item_id: int):
        item = self.service.delete(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
