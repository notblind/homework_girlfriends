from database.models import Post


def get_average_value(parametr, elements):
    return sum([getattr(el, parametr, 0) for el in elements]) / len(elements)


if __name__ == '__main__':
    count_posts = Post.select().count()
    posts_with_photo = Post.select().where((Post.has_photo == True) & (Post.has_video == False))
    posts_with_video = Post.select().where((Post.has_photo == False) & (Post.has_video == True))
    posts_with_only_text = Post.select().where((Post.has_photo == False) & (Post.has_video == False))

    av_likes_with_photo = get_average_value("likes", posts_with_photo)  # Среднее кол-во лайков с фото
    av_reactions_with_photo = get_average_value("reactions", posts_with_photo)  # Среднее кол-во реакций с фото
    av_views_with_photo = get_average_value("views", posts_with_photo)  # Среднее кол-во просмотров с фото

    av_likes_with_video = get_average_value("likes", posts_with_video)  # Среднее кол-во лайков с видео
    av_reactions_with_video = get_average_value("reactions", posts_with_video)  # Среднее кол-во реакций с видео
    av_views_with_video = get_average_value("views", posts_with_video)  # Среднее кол-во просмотров с видео

    a = 10
