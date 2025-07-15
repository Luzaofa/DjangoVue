from django.views import View
from django.http import JsonResponse


class GetActDataView(View):
    '''画廊数据'''

    def get(self, request):
        data = [
            {
                "id": 1,
                "title": "抽象几何",
                "artist": "现代艺术家",
                "year": "2024",
                "image": "https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=800&h=600&fit=crop",
                "description": "探索几何形状与色彩的完美结合",
                "likes": 342,
                "views": 1205
            },
            {
                "id": 2,
                "title": "城市夜景",
                "artist": "摄影大师",
                "year": "2023",
                "image": "https://images.unsplash.com/photo-1514905552197-0610a4d8fd73?w=800&h=600&fit=crop",
                "description": "捕捉都市夜晚的璀璨光影",
                "likes": 891,
                "views": 2547
            },
            {
                "id": 3,
                "title": "自然之美",
                "artist": "风景画家",
                "year": "2024",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop",
                "description": "大自然的壮丽与宁静",
                "likes": 567,
                "views": 1890
            },
            {
                "id": 4,
                "title": "现代雕塑",
                "artist": "雕塑艺术家",
                "year": "2023",
                "image": "https://images.unsplash.com/photo-1578321272176-b7bbc0679853?w=800&h=600&fit=crop",
                "description": "金属与光影的艺术对话",
                "likes": 423,
                "views": 1634
            },
            {
                "id": 5,
                "title": "色彩爆炸",
                "artist": "抽象画家",
                "year": "2024",
                "image": "https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=800&h=600&fit=crop",
                "description": "色彩的狂欢与情感的释放",
                "likes": 721,
                "views": 2198
            }
        ]
        return JsonResponse(data, safe=False)
