from flask import jsonify, request
from models import db
from models.blog_model import Blog
# from sqlalchemy.exc import SQLAlchemyError

def create_blog():
    try:
        # Parse request data
        data = request.get_json()

        # Validate required fields
        required_fields = ['title', 'slug', 'blog_content', 'blog_keywords', 'blog_main_image', 'category']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Create a new blog instance
        new_blog = Blog(
            title=data['title'],
            slug=data['slug'],
            blog_content=data['blog_content'],
            blog_keywords=data['blog_keywords'],
            blog_main_image=data['blog_main_image'],
            category=data['category'],
            is_published=data.get('is_published', False)  # Default to False if not provided
        )

        # Add to database and commit
        db.session.add(new_blog)
        db.session.commit()

        return jsonify({"message": "Blog created successfully", "blog": {
            "id": new_blog.id,
            "title": new_blog.title,
            "slug": new_blog.slug,
            "category": new_blog.category
        }}), 201

    # except SQLAlchemyError as e:
    #     db.session.rollback()  # Rollback in case of an error
    #     return jsonify({"error": "Database error occurred", "details": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500






def fetch_blog_by_slug(slug):
    try:
        # Get the slug from query parameters
        
        # Query the blog by slug
        blog = Blog.query.filter_by(slug=slug).first()

        # Check if the blog exists
        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        # Serialize the blog data
        blog_data = {
            "id": blog.id,
            "title": blog.title,
            "slug": blog.slug,
            "category": blog.category,
            "blog_content": blog.blog_content,
            "blog_keywords": blog.blog_keywords,
            "blog_main_image": blog.blog_main_image,
            "is_published": blog.is_published,
            "created_at": blog.created_at.isoformat() if blog.created_at else None,
            "updated_at": blog.updated_at.isoformat() if blog.updated_at else None,
        }

        # Return the serialized blog as a JSON response
        return jsonify({"blog": blog_data}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500
    




def fetch_all_blogs():
    try:
        # Query all blogs from the database
        blogs = Blog.query.all()
        
        # Serialize the blog data into a list of dictionaries
        blogs_list = [
            {
                "id": blog.id,
                "title": blog.title,
                "slug": blog.slug,
                "category": blog.category,
                "blog_content": blog.blog_content,
                "blog_keywords": blog.blog_keywords,
                "blog_main_image": blog.blog_main_image,
                "is_published": blog.is_published,
                "created_at": blog.created_at.isoformat() if blog.created_at else None,
                "updated_at": blog.updated_at.isoformat() if blog.updated_at else None,
            }
            for blog in blogs
        ]

        # Return the serialized list as a JSON response
        return jsonify({"blogs": blogs_list, "count": len(blogs_list)}), 200

    # except SQLAlchemyError as e:
    #     # Rollback any pending transactions if a database error occurs
    #     db.session.rollback()
    #     return jsonify({"error": "Database error occurred", "details": str(e)}), 500

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500