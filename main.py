edit_message_text(
                f"Страны ({name}):",
                reply_markup=paginated_keyboard(countries, 0, back="back_cont")
            )

        # Level: country
        if user["level"]=="country":
        cont=user["continent"]
            if name in DB[cont]:
            user["level"]="brand"
            user["country"]=name
            user["page"]=0

                brands=list(DB[cont][name].keys())
                return await query.edit_message_text(
                    f"Марки ({name}):",
                    reply_markup=paginated_keyboard(brands, 0, back="back_country")
                )

        # Level: brand
        if user["level"]==brand":
        cont = user["continent"]
        cnt = user["country"]
            if name in DB[cont][cnt]:
            link = DB[cont][cnt][name]
                return await query.edit_message_text(
                    f"Марка: {name}\nСайт: {link}"
                )


async def main():
    app = ApplicationBuilder().token("BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback))

    await app.run_polling()


if name == "__main__":
import asyncio
asyncio.run(main())
