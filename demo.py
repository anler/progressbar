import progressbar


FILESIZE = 2045824
CHUNK = 1


def main():
    progress = progressbar.AnimatedProgressBar(end=FILESIZE, width=50)

    for i in range(0, FILESIZE, CHUNK):
        progress + CHUNK
        progress.show_progress()


if __name__ == "__main__":
    main()
