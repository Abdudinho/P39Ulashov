from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from dispetcher import dp


orders = [
    {
        "id": 1,
        "title": 'Product1',
        "price": 1000,
        'quantity' : 2
    }
]

@dp.message(Command('payment'))
async def command_start_handler(message: Message) -> None:
    # order_id = int(message.text.split()[1].split('_')[1])
    CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"

    prices = []
    for order_item in orders:
        prices.append(LabeledPrice(label=order_item.get("title"), amount=order_item.get("price")*order_item.get("quantity")*100),)

    await message.answer_invoice('Products', description=f"Productlar soni {len(orders)}", payload=str(1), currency="UZS",provider_token=CLICK_TOKEN,prices= prices)

@dp.pre_checkout_query()
async def success_handler(pre_checkout_query: PreCheckoutQuery) -> None:
    await pre_checkout_query.answer(True)


@dp.message(lambda message: bool(message.successful_payment))
async def confirm_handler(message: Message):
    if message.successful_payment:
        total_amount = message.successful_payment.total_amount//100
        order_id = int(message.successful_payment.invoice_payload)
        # await sync_to_async(Order.objects.filter(id=order_id).update)(status=Order.StatusType.COMPLETED)
        await message.answer(text=f"To'lo'vingiz uchun raxmat 😊 \n{total_amount}\n{order_id}")


print("Payment bu ")