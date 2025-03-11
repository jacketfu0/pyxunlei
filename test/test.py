
from pyxunlei import XunLeiClient


if __name__ == "__main__":
    xunlei_client = XunLeiClient(
        '192.168.2.137', 2345)
    # print(xunlei_client._torrent2magnet(
    #     "))
    # xunlei_client.download_torrent('/Users/kanhui/Downloads/ubuntu-23.04-live-server-amd64.iso.torrent')
    # print(xunlei_client.completed_tasks())
    xunlei_client.download_magnetic('magnet:?xt=urn:btih:101b16b3a9b023de40d9680d531f5a30ffcd5455&dn=FC2-3363283%20%E3%80%90%E9%96%B2%E8%A6%A7%E6%B3%A8%E6%84%8F%E3%80%91%E6%B8%AF%E5%8C%BA%E5%A5%B3%E5%AD%90%20VS%20%E5%AE%B9%E7%96%91%E8%80%85K%E3%80%82%E3%82%AE%E3%83%A3%E3%83%A9%E9%A3%B2%E3%81%BF%E3%82%A2%E3%83%97%E3%83%AA%E3%81%A7%E5%87%BA%E4%BC%9A%E3%81%A3%E3%81%9F%E8%89%B2%E7%99%BD%E7%BE%8E%E4%BA%BA%E3%81%8C%E5%97%9A%E5%92%BD%EF%BC%81%E9%81%8E%E5%91%BC%E5%90%B8%EF%BC%81%E5%8F%A3%E3%81%8B%E3%82%89%E3%81%AF%E3%82%A4%E3%83%A9%E3%83%9E%E6%B1%81%E3%83%80%E3%83%A9%E3%83%80%E3%83%A9%E3%81%AE%E5%A4%A7%E5%8F%B7%E6%B3%A3%EF%BC%81%E3%80%8C%E5%8B%95%E7%94%BB..%E6%B6%88%E3%81%97%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E2%80%A6%E3%80%8D%E6%B6%99%E3%81%AE%E8%A8%B4%E3%81%88%E3%82%82%E3%81%BE%E3%81%95%E3%81%8B%E3%81%AE%E6%B5%81%E5%87%BA%E3%80%82&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%',sub_dir='FC2-3363283',
                                    preprocess_files=xunlei_client.filter_file_by_size)
