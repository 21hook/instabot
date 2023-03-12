from instapy import InstaPy
from instapy import smart_run

class InstagramBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)

    @smart_run
    def search_posts_by_keyword(self, keyword):
        self.session.search_by_tags([keyword])
        posts = self.session.get_instapy_response().get('tags', {}).get(keyword, {}).get('media', [])
        post_ids = [post['node']['id'] for post in posts]
        return post_ids

    @smart_run
    def get_top_comments_of_post(self, post_id):
        comments = self.session.get_media_comments(media_id=post_id, only_text=True, count=50)
        top_comments = sorted(comments, key=lambda c: c.likes_count, reverse=True)[:5]
        comment_ids = [c.id for c in top_comments]
        return comment_ids

    @smart_run
    def read_comment_id(self, comment_id):
        comment = self.session.get_comment(comment_id)
        return comment

    @smart_run
    def comment_on_post(self, post_id, comment_text):
        self.session.comment(post_id=post_id, comment_text=comment_text)

