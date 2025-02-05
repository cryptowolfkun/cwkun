from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ボットのトークン
TOKEN = '7719566704:AAGVXIjkCjqNNpaQk90ZkrUPQ1owEJ5idBo'  # 実際のトークンに置き換えてください
YOUR_CHAT_ID = 7632955063  # あなたのチャットIDに置き換えてください

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('こんにちは！ピン留めされたメッセージを通知します。')

async def pin_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.pinned_message:
        pinned_text = update.message.pinned_message.text
        # あなたのチャットIDにメッセージを送信
        await context.bot.send_message(chat_id=YOUR_CHAT_ID, text=f'新しいピン留めメッセージ: {pinned_text}')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    await update.message.reply_text(f'あなたのチャットIDは {7632955063} です。')

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, pin_message))  # 全てのメッセージを監視
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # テキストメッセージのハンドラー

    app.run_polling()

if __name__ == '__main__':
    main()
