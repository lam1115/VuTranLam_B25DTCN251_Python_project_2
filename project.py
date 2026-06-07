players_list = [
    {
        "id": "CT001",
        "name": "Nguyen Van A",
        "matches": 50,
        "goals": 25,
        "assists": 10,
        "achievement_score": 60,
        "title": ""
    }
]

def hollow_check(value):
    if value.strip() == "":
        print("Không được để trống!")
        return True
    return False


def number_check(value):
    if value < 0:
        print("Giá trị phải >= 0!")
        return True
    return False


def achievement_score_process(goals, assists):
    return goals * 2 + assists


def title_process(score):
    if score > 40:
        return "Vàng"
    elif score > 20:
        return "Bạc"
    else:
        return "Đồng"


def print_player(player):
    print(
        f"Mã: {player['id']:<8} | "
        f"Tên: {player['name']:<20} | "
        f"Trận: {player['matches']:<5} | "
        f"Bàn thắng: {player['goals']:<5} | "
        f"Kiến tạo: {player['assists']:<5} | "
        f"Điểm: {player['achievement_score']:<5} | "
        f"Danh hiệu: {player['title']}"
    )


def display_player_list(player_list):
    if not player_list:
        print("Danh sách cầu thủ đang trống!")
        return

    print("\n===== DANH SÁCH CẦU THỦ =====")

    for index, player in enumerate(player_list, start=1):
        print(f"{index}. ", end="")
        print_player(player)


def add_player(player_list):
    new_player = {}

    while True:
        player_id = input("Nhập mã cầu thủ: ").strip().upper()

        if hollow_check(player_id):
            continue

        if any(player["id"] == player_id for player in player_list):
            print("Mã cầu thủ đã tồn tại!")
            continue

        new_player["id"] = player_id
        break

    while True:
        name = input("Nhập tên cầu thủ: ").strip().title()

        if hollow_check(name):
            continue

        new_player["name"] = name
        break

    while True:
        try:
            matches = int(input("Số trận đấu: "))
            if number_check(matches):
                continue

            goals = int(input("Số bàn thắng: "))
            if number_check(goals):
                continue

            assists = int(input("Số kiến tạo: "))
            if number_check(assists):
                continue

            break

        except ValueError:
            print("Vui lòng nhập số!")

    new_player["matches"] = matches
    new_player["goals"] = goals
    new_player["assists"] = assists

    new_player["achievement_score"] = (
        achievement_score_process(goals, assists)
    )

    new_player["title"] = title_process(
        new_player["achievement_score"]
    )

    player_list.append(new_player)

    print("Thêm cầu thủ thành công!")


def update_player(player_list):
    player_id = input(
        "Nhập mã cầu thủ cần cập nhật: "
    ).strip().upper()

    for player in player_list:

        if player["id"] == player_id:

            while True:
                try:
                    goals = int(
                        input("Bàn thắng mới: ")
                    )

                    if number_check(goals):
                        continue

                    assists = int(
                        input("Kiến tạo mới: ")
                    )

                    if number_check(assists):
                        continue

                    break

                except ValueError:
                    print("Vui lòng nhập số!")

            player["goals"] = goals
            player["assists"] = assists

            player["achievement_score"] = (
                achievement_score_process(
                    goals,
                    assists
                )
            )

            player["title"] = title_process(
                player["achievement_score"]
            )

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy cầu thủ!")


def del_player(player_list):
    player_id = input(
        "Nhập mã cầu thủ cần xóa: "
    ).strip().upper()

    for player in player_list:

        if player["id"] == player_id:

            confirm = input(
                "Bạn có chắc muốn xóa? (Y/N): "
            ).strip().upper()

            if confirm == "Y":
                player_list.remove(player)
                print("Xóa thành công!")
            else:
                print("Đã hủy xóa!")

            return

    print("Không tìm thấy cầu thủ!")


def find_by_id(player_list):
    player_id = input(
        "Nhập mã cầu thủ: "
    ).strip().upper()

    for player in player_list:

        if player["id"] == player_id:
            print_player(player)
            return

    print("Không tìm thấy cầu thủ!")


def find_by_name(player_list):
    keyword = input(
        "Nhập tên cầu thủ: "
    ).strip().lower()

    found = False

    for player in player_list:

        if keyword in player["name"].lower():
            print_player(player)
            found = True

    if not found:
        print("Không tìm thấy cầu thủ!")


def find_player(player_list):

    while True:

        choice = input("""
1. Tìm theo mã
2. Tìm theo tên
3. Quay lại
====================
Mời nhập:
""")

        if not choice.isdigit():
            continue

        choice = int(choice)

        match choice:

            case 1:
                find_by_id(player_list)

            case 2:
                find_by_name(player_list)

            case 3:
                break

            case _:
                print("Lựa chọn không hợp lệ!")


def sort_player(player_list):

    while True:

        choice = input("""
1. Điểm thành tích giảm dần
2. Bàn thắng giảm dần
3. Quay lại
====================
Mời nhập:
""")

        if not choice.isdigit():
            continue

        choice = int(choice)

        match choice:

            case 1:
                player_list.sort(
                    key=lambda x: x["achievement_score"],
                    reverse=True
                )
                print("Đã sắp xếp theo điểm thành tích.")

            case 2:
                player_list.sort(
                    key=lambda x: x["goals"],
                    reverse=True
                )
                print("Đã sắp xếp theo bàn thắng.")

            case 3:
                break

            case _:
                print("Lựa chọn không hợp lệ!")


def stats_title(player_list):

    vang = 0
    bac = 0
    dong = 0

    for player in player_list:

        if player["title"] == "Vàng":
            vang += 1

        elif player["title"] == "Bạc":
            bac += 1

        else:
            dong += 1

    print("\n===== THỐNG KÊ DANH HIỆU =====")
    print(f"Vàng: {vang}")
    print(f"Bạc : {bac}")
    print(f"Đồng: {dong}")


def count_by_title(player_list):

    result = {}

    for player in player_list:

        title = player["title"]

        result[title] = (
            result.get(title, 0) + 1
        )

    print("\n===== SỐ LƯỢNG THEO DANH HIỆU =====")

    for title, count in result.items():
        print(f"{title}: {count}")


def highest_lowest_player(player_list):

    if not player_list:
        print("Danh sách trống!")
        return

    max_score = max(
        player["achievement_score"]
        for player in player_list
    )

    min_score = min(
        player["achievement_score"]
        for player in player_list
    )

    print("\n===== CẦU THỦ NHIỀU DANH HIỆU NHẤT =====")

    for player in player_list:

        if player["achievement_score"] == max_score:
            print_player(player)

    print("\n===== CẦU THỦ ÍT DANH HIỆU NHẤT =====")

    for player in player_list:

        if player["achievement_score"] == min_score:
            print_player(player)


while True:

    choice = input("""
========== QUẢN LÝ CẦU THỦ ==========
1. Hiển thị danh sách cầu thủ
2. Thêm cầu thủ
3. Cập nhật cầu thủ
4. Xóa cầu thủ
5. Tìm kiếm cầu thủ
6. Sắp xếp danh sách
7. Thống kê danh hiệu
8. Thống kê số lượng theo danh hiệu
9. Cầu thủ nhiều/ít danh hiệu nhất
10. Thoát
====================================
Mời nhập lựa chọn:
""")

    if not choice.isdigit():
        continue

    choice = int(choice)

    match choice:

        case 1:
            display_player_list(players_list)

        case 2:
            add_player(players_list)

        case 3:
            update_player(players_list)

        case 4:
            del_player(players_list)

        case 5:
            find_player(players_list)

        case 6:
            sort_player(players_list)

        case 7:
            stats_title(players_list)

        case 8:
            count_by_title(players_list)

        case 9:
            highest_lowest_player(players_list)

        case 10:
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")