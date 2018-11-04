from GetMusicUrl import Music


def main():
    m = Music()
    m.set_id('553755659')
    t = m.get_music_detail()
    print(t)


if __name__ == '__main__':
    main()
