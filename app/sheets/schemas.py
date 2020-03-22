BLUEPRINT_ITEM_TYPES = [
    "TextFrame",
    "SheetTitle",
    "SheetHeader",
]

BLUEPRINT_SCHEMA = {
    'type': 'array',
    'title': 'blueprint',
    'items': {
        'type': 'object',
        'required': [
            'id',
            'type',
            'params',
        ],
        'properties': {
            'id': {
                'title': 'id',
                'type': 'integer',
            },
            'type': {
                'title': 'type',
                'type': 'string',
                'enum': BLUEPRINT_ITEM_TYPES,
            },
            'params': {
                'title': 'params',
                'type': 'object',
                'required': [],
                'properties': {
                    "desc": {
                        'title': 'desc',
                        'type': 'string',
                        'format': 'text',
                    },
                    "title": {
                        'title': 'title',
                        'type': 'string',
                    },
                    "imageURL": {
                        'title': 'imageURL',
                        'type': 'string',
                    },
                }
            },
        }
    }
}