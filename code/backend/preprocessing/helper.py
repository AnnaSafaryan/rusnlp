
def create_title2hash(filename, lower=True):
    title2hash = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            hashcode, title = line.split('\t')[:2]
            conference, year = hashcode.split("_")[:2]
            if lower:
                title = title.lower()
            assert not title2hash.get((title, conference, year)), (title, conference, year)
            title2hash[(title, conference, year)] = hashcode
    return title2hash


def create_hash2url(filename):
    hash2url = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            hashcode, _, url = line.split('\t')
            assert hashcode not in hash2url
            hash2url[hashcode] = url[:-1]
    return hash2url


def create_name2author(filename):
    name2author = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            id_, cluster, name = line[:-1].split("\t")
            assert name not in name2author
            name2author[name] = (id_, cluster)
    return name2author


def create_name2affiliation(filename):
    name2affiliation = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            id_, cluster, name = line[:-1].split("\t")
            assert name not in name2affiliation, f"{id_} {cluster} {name}"
            name = name.replace("\r\n", "").replace("\n", ' ').replace("  ", " ").replace(",  ", "")
            name2affiliation[name] = (id_, cluster)
    return name2affiliation