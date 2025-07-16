class UIResponsiveManager:
    def __init__(self):
        self.breakpoints = [
            {
                'min_w': 0,
                'max_w': 600,
                'min_h': 0,
                'max_h': 600,
                'params': {
                    'groupBox_2': (289, 0, 191, 396),
                    'groupBox_6': (490, 0, 261, 396),
                }
            },
            {
                'min_w': 601,
                'max_w': 2000,
                'min_h': 0,
                'max_h': 2000,
                'params': {
                    'groupBox_2': (10, 10, 250, 400),
                    'groupBox_6': (270, 10, 300, 400),
                }
            }
        ]

    def get_params_for_size(self, width, height):
        for bp in self.breakpoints:
            if (bp['min_w'] <= width <= bp['max_w'] and
                bp['min_h'] <= height <= bp['max_h']):
                return bp['params']
        return None  # or return default params
