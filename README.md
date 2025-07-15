# 🖼 DjangoVue Gallery

**基于 Django + Vue 的分离式画廊应用**  
前端通过 Vue 消费 Django REST API，实现现代化前后端分离架构。

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![Vue](https://img.shields.io/badge/Vue-3-4FC08D)](https://vuejs.org/)
[![REST](https://img.shields.io/badge/API-REST%20ful-FF6B6B)](https://www.django-rest-framework.org/)

## 🌟 核心特性
- **前后端解耦**：Django 提供 RESTful API，Vue 独立渲染前端
- **画廊功能**：图片展示、详情查看、响应式布局
- **数据交互**：Axios 实现 API 请求/响应处理
- **高效开发**：热重载支持 + Django 调试工具

## 🧩 技术栈
| 后端 (Django)          | 前端 (Vue)          |
|----------------------|---------------------|
| Python 3.10+         | Vue 3 Composition API |
| Django 4.2           | Vue Router 4        |
| Django REST Framework | Pinia 状态管理      |
| Sqlite               | Axios 数据请求      |
| CORS Headers         | Tailwind CSS 样式   |

## 🚀 快速启动

### 后端 Django 设置
```bash
# 克隆项目
git clone https://github.com/Luzaofa/DjangoVue.git
cd DjangoVue

# 迁移数据库
python manage.py migrate

# 运行开发服务器
python manage.py runserver
```

### 前端 Vue 设置 
```bash
cd ../frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

