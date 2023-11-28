from settings import db_handle
from models import Group, Post


groups = (
    ("160814627", "Ленинградский Электромемический Институт", "electromeme"),
    ("186266211", "Факультет Мемологии СПбГУ", "memes_spbu"),
    ("127149194", "ИТМЕМ", "itmem"),
    ("219697224", "Факультет Мемологии СПБГУ I СПБГУ МЕМЫ", "spbu_memas"),
    ("153165581", "Питер Зе Греат Мемес", "peterthergreatmemes"),
    ("88037184", "ПГУПС MEMES", "memes_pgups"),
    ("170087794", "Мольберт | СПбГУПТД", "molbert_ptd"),
    ("146208019", "Memgut", "bonchmemes"),
    ("99416513", "гэу мемес", "uneconmemes"),
    ("216702599", "СЗИУ КЕБаБ при Президенте", "sziukebab"),
    ("221740693", "Кафедра мемологии РГПУ им. А.И. Герцена", "uniherzen_mem"),
)


if __name__ == '__main__':
    with db_handle.atomic():
        Group.create_table()
        Post.create_table()

        Group.insert_many(
            groups, fields=[Group.resource_id, Group.name, Group.screen_name]
        ).execute()

