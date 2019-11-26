def Router(app):
    from views.apis.mirrors import register, register_char, todo, todo_check, stuff, shop
    app.register_blueprint(register.api.blueprint)
    app.register_blueprint(register_char.api.blueprint)
    app.register_blueprint(todo.api.blueprint)
    app.register_blueprint(todo_check.api.blueprint)
    app.register_blueprint(stuff.api.blueprint)
    app.register_blueprint(shop.api.blueprint)