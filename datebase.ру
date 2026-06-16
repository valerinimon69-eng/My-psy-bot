import aiosqlite

async def init_db():
    async with aiosqlite.connect("psy_bot.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT)")
        await db.execute("CREATE TABLE IF NOT EXISTS appointments (app_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, date TEXT)")
        await db.commit()
