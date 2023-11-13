def test_add_product(product_repo, get_random_item):
    db = product_repo
    db.insert_one(**get_random_item)
    prd = db.get_one_by_id(get_random_item['item_id'])
    assert prd == tuple(get_random_item.values())


def test_get_all_employee(product_repo):
    db = product_repo
    all_prd = db.get_all()
    assert isinstance(all_prd, list)


def test_select_product(product_repo, get_random_item_id):
    db = product_repo
    prod_id = get_random_item_id
    product = db.get_one_by_id(prod_id)
    assert product[0] == prod_id


def test_delete_product(get_random_item_id, product_repo):
    db = product_repo
    tab_before = len(db.get_all())
    deleted_product = db.delete_product(get_random_item_id)
    tab_after = len(db.get_all())
    assert deleted_product is None
    assert tab_after == tab_before - 1


def test_update_product(product_repo, get_random_item_id, get_random_item):
    db = product_repo
    item_id = get_random_item_id
    _, *rest_of_values = get_random_item.items()
    db.update_product(item_id, **dict(rest_of_values))
    prd = db.get_one_by_id(item_id)
    assert prd[1:] == tuple(dict(rest_of_values).values())


def test_select_void_product(product_repo):
    db = product_repo
    void_product = db.get_one_by_id(0)
    assert void_product is None


def test_delete_void_product(product_repo):
    db = product_repo
    tab_before = len(db.get_all())
    db.delete_product(0)
    tab_after = len(db.get_all())
    assert tab_after == tab_before
