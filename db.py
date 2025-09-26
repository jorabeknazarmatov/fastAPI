from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models import User, Post
from sqlalchemy import create_engine
from log import logger
import config

engine = create_engine(config.url, echo=False)


class DB_CRUD():
    def __init__(self):
        self.sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    
    def all_users(self):
        with self.sessionLocal() as session:
            users = session.query(User).all()
            
            return [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    
    def add_user(self, name: str, email: str):
        with self.sessionLocal() as session:
            user = User(name = name, email = email)
            try:
                session.add(user)
                session.commit()
            except IntegrityError:
                session.rollback()
                logger.error("Email ro'yxatdan o'tgan")
                raise HTTPException(status_code=409, detail="Email already exists")
            
            logger.info(f"{name} ismli foydalanuvchi qo'shildi")
            return {"id": user.id, "name": user.name, "email": user.email}
    
    def update_name(self, id: int, name: str):
        with self.sessionLocal() as session:
            user = session.get(User, id)
            
            if not user:
                logger.error(f'Bunday id={id} foydalanuvchi topilmadi')
                raise HTTPException(status_code=404, detail="User not found")
            
            temp = user.name
            user.name = name
            session.commit()
            logger.info(f"Foydalanuvchining ismi {temp} dan {user.name} ga o'zgartirildi")
            return {"id": user.id, "name": user.name}
                
    def del_user(self, id: int):
        with self.sessionLocal() as session:
            user = session.get(User, id)
            if not user:
                logger.error(f'Bunday id={id} foydalanuvchi topilmadi')
                raise HTTPException(status_code=404, detail="User not found")
            session.delete(user) # ORM cascade ishlaydi
            session.commit()
            logger.info(f"Foydalanuvchi {user.name} o'chirildi")
            return {"status": "deleted"}
      
    def add_posts(self, id: int, post_title: str, post_content: str):
        with self.sessionLocal() as session:
            user = session.query(User).filter_by(id = id).first()
            
            if user is None:
                logger.error(f"Bunday id={id} foydalanuvchi topilmadi")
                raise HTTPException(status_code=404, detail="User not found")

            
            post = Post(title = post_title, content = post_content, user = user)
            session.add(post)
            session.commit()
            logger.info(f"Post qo‘shildi: {post_title}")
            return {"id": post.id, "title": post.title}