def note_detail(note) -> dict:
    return {
        '_id': str(note['_id']),
        'user_id': note['user_id'],
        'target_id': note['target_id'],
        'key': note['key'],
        'data': note['data'],
        'timestamp': note['timestamp'],
        'is_new': note['is_new']
    }


def notes_list(notes) -> list:
    return [note_detail(note) for note in notes]
