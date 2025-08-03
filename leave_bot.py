from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

ADMIN_CHAT_ID = 767044746  
BOT_TOKEN = '8240597137:AAF414fTbrsAFtJIhUmDsRNjR-m4-uYz_Xc'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 *Welcome to the NOC Leave Request Bot*\n"
        "You can request:\n\n"
        "📅 *Leave* — use this format:\n"
        "```\n"
        "Date: YYYY-MM-DD\n"
        "Reason: Your reason here\n"
        "```\n\n"
        "🔁 *Swap Duty* — use this format:\n"
        "```\n"
        "Swap: YYYY-MM-DD\n"
        "With: @username\n"
        "Reason: Your reason here\n"
        "```",
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    if "date" in text.lower() and "reason" in text.lower():
        # Send leave request to admin
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"📩 Leave request from {user.first_name} (@{user.username}):\n{text}"
        )
        await update.message.reply_text("✅ Your leave request has been sent.")
    else:
        await update.message.reply_text("❗ Please follow the format:\nDate: YYYY-MM-DD\nReason: ...")
        if "swap" in text.lower() and "with" in text.lower():
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"🔁 Swap request from {user.first_name} (@{user.username}):\n{text}"
    )
    await update.message.reply_text("🔁 Your swap request has been sent.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot is running. Press Ctrl+C to stop.")
    app.run_polling()


