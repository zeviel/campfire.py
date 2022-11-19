import requests

class Campfire:
	def __init__(self) -> None:
		self.api = "https://campfire.moe/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
			"accept": "application/json"
		}
		self.user_id = None
		self.nickname = None
		self.access_token = None
		self.login_token = None

	def login(self, email: str, password: str) -> dict:
		data = {
			"email": email,
			"password": password,
			"redir": False
		}
		response = requests.post(
			f"{self.api}/auth/login",
			data=data,
			headers=self.headers)
		json = response.json()
		cookies = response.cookies
		if "account" in json:
			self.user_id = json["account"]["J_ID"]
			self.nickname = json["account"]["J_NAME"]
			self.access_token = cookies["token"]
			self.login_token = cookies["loginToken"]
			self.headers["J_API_ACCESS_TOKEN"] = self.access_token
			self.headers["J_API_LOGIN_TOKEN"] = self.login_token
		return json

	def comment(
			self,
			pub_id: int,
			content: str,
			reply_id: int = 0) -> dict:
		return requests.post(
			f"{self.api}/pub/{pub_id}/comment?redir=false",
			headers=self.headers).json()

	def get_draft_content(self, draft_id: int) -> dict:
		return requests.get(
			f"{self.api}/drafts/{draft_id}",
			headers=self.headers).json()

	def publish_post(self, draft_id: int) -> dict:
		return requests.get(
			f"{self.api}/draft/{draft_id}/publish",
			headers=self.headers).json()

	def get_my_profile(self) -> dict:
		return requests.get(
			f"{self.api}/user",
			headers=self.headers).json()

	def get_my_quest(self) -> dict:
		return requests.get(
			f"{self.api}/user/quest",
			headers=self.headers).json()

	def send_karma(self, pub_id: int, is_positive: bool) -> dict:
		return requests.get(
			f"{self.api}/pub/{pub_id}/karma?positive={is_positive}",
			headers=self.headers).json()

	def reject_activity(self, activity_id: int) -> dict:
		return requests.get(
			f"{self.api}/activity/{activity_id}/reject",
			headers=self.headers).json()

	def sub_fandom(
			self,
			fandom_id: int,
			type: str = "all",
			important: bool = True) -> dict:
		return requests.get(
			f"{self.api}/fandom/{fandom_id}/sub?type={type}&important={important}",
			headers=self.headers).json()

	def member_activity(
			self,
			activity_id: int, 
			is_member: bool) -> dict:
		return requests.get(
			f"{self.api}/activity/{activity_id}/member?member={is_member}",
			headers=self.headers).json()

	def get_my_drafts(self, offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/drafts?offset={offset}",
			headers=self.headers).json()

	def get_feed(
			self,
			type: str = "all",
			offset: int = 0) -> dict:
		"""
		FEED-TYPES:
			 1 - ALL,
			 2 - SUBSCRIBED,
			 3 - GOOD,
			 4 - BEST,
			 5 - ALL_SUBS,
			 6 - ABYSS
		"""
		return requests.get(
			f"{self.api}/feed?type={type}&offset={offset}",
			headers=self.headers).json()

	def get_account_info(self, nickname: str) -> dict:
		return requests.get(
			f"{self.api}/account/{nickname}",
			headers=self.headers).json()

	def get_account_posts(
			self,
			account_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/account/{account_id}/publications?offset={offset}",
			headers=self.headers).json()

	def get_activity_info(self, activity_id: int) -> dict:
		return requests.get(f"{self.api}/activity/{activity_id}",
			headers=self.headers).json()

	def get_activity_posts(
			self,
			activity_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/activity/{activity_id}/posts?offset={offset}",
			headers=self.headers).json()

	def get_fandom_info(self, fandom_id: int) -> dict:
		return requests.get(
			f"{self.api}/fandom/{fandom_id}",
			headers=self.headers).json()

	def get_fandom_posts(
			self,
			fandom_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/fandom/{fandom_id}/posts?offset={offset}",
			headers=self.headers).json()

	def get_fandom_wiki(
			self,
			fandom_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/fandom/{fandom_id}/wiki?offset={offset}", 
			headers=self.headers).json()

	def get_fandom_wiki_section(
			self,
			fandom_id: int,
			section_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/fandom/{fandom_id}/wiki/{section_id}?offset={offset}",
			headers=self.headers).json()

	def get_wiki_articles(self, article_id: int) -> dict:
		return requests.get(
			f"{self.api}/fandom/wiki/{article_id}",
			headers=self.headers).json()

	def get_popular_fandoms(
			self,
			card: bool = False,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/fandom?card={card}&offset={offset}",
			headers=self.headers).json()

	def get_image(self, image_id: int) -> dict:
		return requests.get(
			f"{self.api}/image/{image_id}",
			headers=self.headers).json()

	def search_posts(self, query: str) -> dict:
		return requests.get(
			f"{self.api}/post/search?q={query}",
			headers=self.headers).json()

	def get_post_content(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/post/{post_id}",
			headers=self.headers).json()

	def get_comments(
			self,
			pub_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/post/{post_id}/comments?offset={offset}",
			headers=self.headers).json()

	def get_project_donates(self) -> dict:
		return requests.get(
			f"{self.api}/project/donates",
			headers=self.headers).json()

	def get_rubric_info(
			self,
			rubric_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/rubric/{rubric_id}?offset={offset}", 
			headers=self.headers).json()

	def get_rubric_posts(
			self,
			rubric_id: int,
			offset: int = 0) -> dict:
		return requests.get(
			f"{self.api}/rubric/{rubric_id}?offset={offset}",
			headers=self.headers).json()
