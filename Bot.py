import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("7716308655:AAGcwNN-3Qd1Ya-Ua_7hjiXdObLon-uVKL8")

if not BOT_TOKEN:
    raise ValueError("TG_TOKEN env variable missing")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات پایتونی‌ام 🚀")

# هر پیام متنی
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    # اینجا می‌توانی هوش مصنوعی یا جستجوی جزوه را صدا بزنی
    if "ریاضی" in text:
        await update.message.reply_text("این جزوه ریاضی شماست: https://example.com/math.pdf")
    else:
        await update.message.reply_text(f"پیام شما: {text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot started…")
    app.run_polling()
