from fastapi import APIRouter
from src.config import settings
from src.http_client import CMCHTTPClient

router = APIRouter(
    prefix="/v1",
)

@router.get('/getListings',
            summary="Get crypto listings")
async def get_listings():
    client = CMCHTTPClient(settings.CMC_BASE_URL, settings.CMC_TOKEN_API)
    try:
        listings = await client.get_listings()
        return listings
    finally:
        await client.close()

@router.get('/getCurrencyInfo/<int:id>',
            summary="Get crypto currency info")
async def get_currency_info(currency_id: int):
    client = CMCHTTPClient(settings.CMC_BASE_URL, settings.CMC_TOKEN_API)
    try:
        currency_info = await client.get_currency_info(currency_id)
        return currency_info
    finally:
        await client.close()

@router.get('/getCurrencyLogo/<int:id>',
            summary='Get crypto currency logo')
async def get_currency_info(currency_id: int):
    client = CMCHTTPClient(settings.CMC_BASE_URL, settings.CMC_TOKEN_API)
    try:
        currency_logo = await client.get_currency_logo(currency_id)
        return currency_logo
    finally:
        await client.close()

@router.get('/getCurrency/<int:id>',
            summary='Get crypto currency')
async def get_currency(currency_id: int):
    client = CMCHTTPClient(settings.CMC_BASE_URL, settings.CMC_TOKEN_API)
    try:
        currency = await client.get_currency(currency_id)
        return currency
    finally:
        await client.close()