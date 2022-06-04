import json


def get_post_all():
    """возвращает посты"""
    with open('./data.json', encoding='utf-8') as infile:
        out = []
        for item in json.load(infile):
            if "#" in item.get('content'):
                out.append(get_tags_in_text(item))
            else:
                out.append(item)
        return out


def get_post_by_user(user_name):
    """возвращает посты определенного пользователя"""
    return [post for post in get_post_all()
            if user_name.lower() == post.get('poster_name').lower()]


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    with open('./comments.json', encoding='utf-8') as infile:
        return [line for line in json.loads(infile.read())
                if line.get('post_id') == post_id]


def search_for_posts(query='к'):
    """возвращает список постов по ключевому слову"""
    return [post for post in get_post_all()
            if query.lower() in post.get('content').split(" ")]


def get_post_by_pk(pk):
    """возвращает список постов по ключевому слову"""
    for post in get_post_all():
        if post.get('pk') == pk:
            return post


def get_tags_in_text(content):
    """Добавляет ссылку к тегу"""
    end_a = '</a>'
    out = []
    for word in content['content'].split(" "):
        if word.startswith('#'):
            start_a = f'<a class="item__tag" href="/tag/?tag={word.replace("#", "")}">'
            out.append(f"{start_a}{word}{end_a}")
        else:
            out.append(word)
    content['content'] = ' '.join(out)
    return content


def find_posts_by_tag(query):
    """возвращает список постов по тегу"""
    return [post for post in get_post_all()
            if f'#{query.lower()}' in post.get('content')]


def get_bookmarks():
    """возвращает список постов, находящихся в закладках"""
    with open('./bookmarks.json', encoding='utf-8') as infile:
        return json.load(infile)


def add_bookmark(postid):
    """добавляет пост в закладки"""
    with open('./bookmarks.json', encoding='utf-8') as infile:
        listobj = list(json.load(infile))
        if {'pk': postid} not in listobj:
            listobj.append({'pk': postid})
    with open('./bookmarks.json', 'w', encoding='utf-8') as outfile:
        json.dump(listobj, outfile, indent=4, separators=(',', ': '))


def delete_bookmark(postid):
    """удаляет пост из закладок"""
    with open('./bookmarks.json', encoding='utf-8') as infile:
        listobj = list(json.load(infile))
        listobj.remove({'pk': postid})
    with open('./bookmarks.json', 'w', encoding='utf-8') as outfile:
        json.dump(listobj, outfile, indent=4, separators=(',', ': '))


def count_bookmarks():
    """возвращает количество закладок"""
    with open('./bookmarks.json', encoding='utf-8') as infile:
        return len(json.load(infile))
