# Blog App - Iteration 5
# Features: Add, View, Delete, Menu Loop, Error Handling

# Data store karne ke liye list
blog_posts = []

def show_menu():
    print("\n" + "="*20)
    print(" 🖋️  MY BLOG APP")
    print("="*20)
    print("1. Add New Post")
    print("2. View All Posts")
    print("3. Delete a Post")
    print("4. Exit")
    print("="*20)

def add_post():
    print("\n--- Create New Post ---")
    title = input("Enter Blog Title: ")
    content = input("Enter Content: ")
    author = input("Enter Author Name: ")
    
    # Dictionary structure for a post
    post = {
        "id": len(blog_posts) + 1,
        "title": title,
        "content": content,
        "author": author
    }
    blog_posts.append(post)
    print("✅ Post added successfully!")

def view_posts():
    print("\n--- All Blog Posts ---")
    if not blog_posts:
        print("📭 No posts available yet.")
        return

    for post in blog_posts:
        print(f"\nID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Author: {post['author']}")
        print(f"Content: {post['content']}")
        print("-" * 15)

def delete_post():
    view_posts()
    if not blog_posts:
        return
        
    try:
        post_id = int(input("\nEnter the ID of the post to delete: "))
        # Check if ID exists
        found = False
        for post in blog_posts:
            if post['id'] == post_id:
                blog_posts.remove(post)
                print(f"🗑️ Post {post_id} deleted!")
                found = True
                break
        
        if not found:
            print("❌ Invalid ID! Post not found.")
            
    except ValueError:
        print("⚠️ Error: Please enter a valid number for ID.")

# --- Main App Loop (The Heart ❤️) ---
def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_post()
        elif choice == '2':
            view_posts()
        elif choice == '3':
            delete_post()
        elif choice == '4':
            print("👋 Goodbye! See you again.")
            break
        else:
            print("❌ Invalid choice, please try again.")

# App Start
if __name__ == "__main__":
    main()