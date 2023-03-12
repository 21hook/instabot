import instaloader

class InstagramBot:
    def __init__(self, username, password):
        self.loader = instaloader.Instaloader()
        self.loader.context.login(username, password)

    def search_posts_by_keyword(self, keyword):
        posts = self.loader.context.get_hashtag_posts(keyword)
        post_ids = [post.shortcode for post in posts]
        return post_ids

    def get_top_comments_of_post(self, post_id):
        post = instaloader.Post.from_shortcode(self.loader.context, post_id)
        comments = post.get_comments()
        top_comments = sorted(comments, key=lambda c: c.likes_count, reverse=True)[:5]
        comment_ids = [c.id for c in top_comments]
        return comment_ids

    def read_comment_id(self, comment_id):
        comment = instaloader.Comment.from_id(self.loader.context, comment_id)
        return comment.text

    def comment_on_post(self, post_id, comment_text):
        post = instaloader.Post.from_shortcode(self.loader.context, post_id)
        post.add_comment(comment_text)

