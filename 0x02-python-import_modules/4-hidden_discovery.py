#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    for u_list in lists:
        if u_list[0:2] != "__":
            print(u_list)
