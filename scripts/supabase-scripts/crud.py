from supabase import Client
from typing import List, Dict


class CRUDservice():
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def add_bulk_negative_images(self, img_urls: List[Dict[str, str]]):
        '''
        img_urls: List = [{"img_url": "..."}]  #Note that the key must be "img_url" (no 's')
        '''
        try:
            response = (
                self.supabase.table("negative")
                .insert(img_urls)
            ).execute()
            return response
        except Exception as e:
            return e