import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db.modules import engine, User, Product
from web.provider import UsernameAndPasswordProvider

app = Starlette()

admin = Admin(engine=engine,
              title="Admin Panel",
              base_url='/',
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="qewrerthytju4")])




class AllModelView(ModelView):
    exclude_fields_from_create = ["created_at" , 'updated_at' , "products"]


admin.add_view(AllModelView(User))
admin.add_view(AllModelView(Product))


admin.mount_to(app)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
