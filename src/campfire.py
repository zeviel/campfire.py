import requests


class Client:
    def __init__(self):
        self.api = "https://campfire.moe/api"
        self.user_id = None
        self.nickname = None
        self.access_token = None
        self.login_token = None

    def login(self, email: str, password: str):
        data = {
            "email": email,
            "password": password,
            "redir": False
        }
        response = requests.post(f"{self.api}/auth/login", data=data)
        json = response.json()
        cookies = response.cookies
        self.user_id = json["account"]["J_ID"]
        self.nickname = json["account"]["J_NAME"]
        self.access_token = cookies["token"]
        self.login_token = cookies["loginToken"]
        return json

    def comment(self, pub_id: int, content: str, reply_id: int = 0):
        return requests.post(
            f"{self.api}/pub/{pub_id}/comment?redir=false").json()

    def get_draft_content(self, draft_id: int):
        return requests.get(f"{self.api}/drafts/{draft_id}").json()

    def publish_post(self, draft_id: int):
        return requests.get(f"{self.api}/draft/{draft_id}/publish").json()

    def get_my_profile(self):
        return requests.get(f"{self.api}/user").json()

    def get_my_quest(self):
        return requests.get(f"{self.api}/user/quest").json()

    def send_karma(self, pub_id: int, is_positive: bool):
        return requests.get(
            f"{self.api}/pub/{pub_id}/karma?positive={is_positive}").json()

    def reject_activity(self, activity_id: int):
        return requests.get(f"{self.api}/activity/{activity_id}/reject").json()

    def sub_fandom(
            self,
            fandom_id: int,
            type: str = "all",
            important: bool = True):
        return requests.get(
            f"{self.api}/fandom/{fandom_id}/sub?type={type}&important={important}").json()

    def member_activity(self, activity_id: int, is_member: bool):
        return requests.get(
            f"{self.api}/activity/{activity_id}/member?member={is_member}").json()

    def get_my_drafts(self, offset: int = 0):
        return requests.get(f"{self.api}/drafts?offset={offset}").json()

    # feed_types: subscribed, all, good, best, all_subs, abyss

    def get_feed(self, type: str = "all", offset: int = 0):
        return requests.get(
            f"{self.api}/feed?type={type}&offset={offset}").json()

    def get_account_info(self, nickname: str):
        return requests.get(f"{self.api}/account/{nickname}").json()

    def get_account_posts(self, account_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/account/{account_id}/publications?offset={offset}").json()

    def get_activity_info(self, activity_id: int):
        return requests.get(f"{self.api}/activity/{activity_id}").json()

    def get_activity_posts(self, activity_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/activity/{activity_id}/posts?offset={offset}").json()

    def get_fandom_info(self, fandom_id: int):
        return requests.get(f"{self.api}/fandom/{fandom_id}").json()

    def get_fandom_posts(self, fandom_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/fandom/{fandom_id}/posts?offset={offset}").json()

    def get_fandom_wiki(self, fandom_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/fandom/{fandom_id}/wiki?offset={offset}").json()

    def get_fandom_wiki_section(
            self,
            fandom_id: int,
            section_id: int,
            offset: int = 0):
        return requests.get(
            f"{self.api}/fandom/{fandom_id}/wiki/{section_id}?offset={offset}").json()

    def get_wiki_articles(self, article_id: int):
        return requests.get(f"{self.api}/fandom/wiki/{article_id}").json()

    # Returns a list of popular fandoms. use card to shuffle it
    def get_popular_fandoms(self, card: bool = False, offset: int = 0):
        return requests.get(
            f"{self.api}/fandom?card={card}&offset={offset}").json()

    def get_image(self, image_id: int):
        return requests.get(f"{self.api}/image/{image_id}").json()

    def search_posts(self, query: str):
        return requests.get(f"{self.api}/post/search?q={query}").json()

    def get_post_content(self, post_id: int):
        return requests.get(f"{self.api}/post/{post_id}").json()

    def get_comments(self, pub_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/post/{post_id}/comments?offset={offset}").json()

    def get_project_donates(self):
        return requests.get(f"{self.api}/project/donates")

    def get_rubric_info(self, rubric_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/rubric/{rubric_id}?offset={offset}").json()

    def get_rubric_posts(self, rubric_id: int, offset: int = 0):
        return requests.get(
            f"{self.api}/rubric/{rubric_id}?offset={offset}").json()
