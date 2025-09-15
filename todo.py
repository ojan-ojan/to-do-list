def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    print("\n--- Daftar Tugas ---")
    if not tasks:
        print("Belum ada tugas.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print(f"Tugas '{task}' ditambahkan!\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Nomor tugas yang ingin dihapus: "))
        removed = tasks.pop(num - 1)
        print(f"Tugas '{removed}' dihapus.\n")
    except (ValueError, IndexError):
        print("Nomor tidak valid.\n")


def main():
    tasks = load_tasks()

    while True:
        print("Menu To-Do List:")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tugas disimpan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.\n")


if __name__ == "__main__":
    main()
