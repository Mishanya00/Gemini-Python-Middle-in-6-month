import asyncio
from pprint import pprint

from pydantic import BaseModel, Field, PositiveInt
import aiohttp
from yarl import URL


class GetCatFactRequestSchema(BaseModel):
    max_length: PositiveInt = Field(gt=0, le=2048)


class GetCatFactResponseSchema(BaseModel):
    fact: str
    length: PositiveInt = Field(gt=0, le=2048)


class GetCatFactsRequestSchema(BaseModel):
    max_length: PositiveInt = Field(gt=0, le=2048)
    limit: PositiveInt = Field(gt=0, le=20)


class GetCatFactsResponseSchema(BaseModel):
    data: list[dict]


class CatClient():
    def __init__(self, session: asyncio.ClientSession):
        self._session = session
        self._base_url = URL('https://catfact.ninja')

    async def fetch_fact(
            self,
            params: GetCatFactRequestSchema
    ) -> GetCatFactResponseSchema:
        params = params.model_dump(by_alias=True)
        print(params)
        async with self._session.get(self._base_url / "fact", params=params) as resp:
            data = await resp.json()

            try:
                return GetCatFactResponseSchema.model_validate(data)
            except ValidationError as e:
                print('[CatClient ERROR] fetch_fact response is not validated.')
                raise e

    # async def fetch_cat_facts():
    #     async with session.get(BASE_URL / "facts", params=params) as resp:
    #         return await resp.json()


async def main():
    params = GetCatFactRequestSchema(
        max_length=512,
    )

    async with aiohttp.ClientSession() as session:
        cat_client = CatClient(session=session)
        cat_fact = await cat_client.fetch_fact(params)
        pprint(cat_fact)


if __name__ == '__main__':
    asyncio.run(main())