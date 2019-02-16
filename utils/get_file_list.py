import os


def get_file_list(file_dir=".", file_type=".wav"):
    all_list = []
    def _get_file(file_dir, file_type=".wav"):
        f_list = os.listdir(file_dir)
        for f in f_list:
            tmp = os.path.join(file_dir, f)
            if os.path.isfile(tmp) and os.path.splitext(tmp)[1] == file_type:
                all_list.append(tmp)
            elif os.path.isdir(tmp):
                _get_file(tmp, file_type)
    _get_file(file_dir, file_type)
    return all_list

