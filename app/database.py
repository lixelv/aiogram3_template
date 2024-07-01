import aiosqlite
import asyncio


class AsyncDB:
    def __init__(self, db_path):
        self.db_path = db_path

    async def do(self, query, params=None):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.cursor() as cursor:
                if params:
                    await cursor.execute(query, params)
                else:
                    await cursor.execute(query)
                await db.commit()

    async def read(self, query, params=None, fetchone=False):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.cursor() as cursor:
                if params:
                    await cursor.execute(query, params)
                else:
                    await cursor.execute(query)

                if fetchone:
                    result = await cursor.fetchone()
                else:
                    result = await cursor.fetchall()

                return result


class TranslateDB(AsyncDB):
    def __init__(self, db_path):
        super().__init__(db_path)
        asyncio.run(self.create_db())

    async def create_db(self):
        await self.do(""" 
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                lang TEXT NOT NULL,
                name TEXT NOT NULL,
                registration_date TEXT NOT NULL
            );""")

    # region user
    async def add_user(self, user_id, name, lang, registration_date):
        await self.do(
            "INSERT INTO user (id, name, lang, registration_date) VALUES (?, ?, ?, ?)",
            (user_id, name, lang, registration_date),
        )

    async def user_exists(self, user_id):
        return bool(
            await self.read(
                "SELECT * FROM user WHERE id = ?", (user_id,), fetchone=True
            )
        )

    async def get_lang(self, user_id):
        return (
            await self.read(
                "SELECT lang FROM user WHERE id = ?", (user_id,), fetchone=True
            )
        )[0]

    async def change_lang(self, user_id, lang):
        await self.do("UPDATE user SET lang = ? WHERE id = ?", (lang, user_id))

    # endregion


db = TranslateDB("db.db")
