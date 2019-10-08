from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://itsgoingdown.org/feed/podcast"
url2 = "http://feeds.feedburner.com/Solecast"
url3 = "https://crimethinc.com/podcast/feed"
url4 = "https://crimethinc.com/podcast/feed"
url5 = "http://thefinalstrawradio.libsyn.com/rss"
url6 = "http://feeds.soundcloud.com/users/soundcloud:users:281599401/sounds.rss"
url7 = "http://feeds.feedburner.com/resonanceaudiodistro"
url8 = "http://wfhb.org/category/news/kiteline/feed/"
url9 = "http://feeds.feedburner.com/RebelBeatRadioPodcasts"
url11 = "https://sub.media/c/submedia-podcasts/feed/"
url12 = "https://sub.media/c/trouble/feed/"
url13 = "http://feeds.soundcloud.com/users/soundcloud:users:301925958/sounds.rss"
url14 = "https://rss.whooshkaa.com/rss/podcast/id/4742"
url15 = "http://www.dissidentisland.org/?feed=show"
url16 = "https://primalanarchy.org/podcast?format=rss"
url17 = "http://feeds.soundcloud.com/users/soundcloud:users:318825005/sounds.rss"
url18 = "https://feed.pippa.io/public/shows/5cd3502455b9e4f12ddc860e"
url19 = "http://fromembers.libsyn.com/rss"
url20 = "http://coffeewithcomrades.com/rss"
url21 = "https://www.spreaker.com/show/3233143/episodes/feed"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2019/05/igdlogo.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2019/03/newlogo-150x150.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/03/full-size1400px-150x150.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://cloudfront.crimethinc.com/assets/podcast/hotwire-1/hotwire-1.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/07/tfsradio-150x150.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/08/rar-150x150.png"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/03/podcast-logo-copy-150x150.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/07/KiteLineLOGO_square-2-150x150.jpg"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/03/rebel-beat-150x150.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2017/06/Itunes-Logo-1-150x150.jpg"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://i0.wp.com/sub.media/wp-content/uploads/2017/05/trouble_podcast_logo.jpg?resize=150%2C150&ssl=1"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/01/26229515_158476234793680_8757692315994236509_n.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/05/subversion1312.png"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/01/Logo_large-150x150.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/05/JPEG-Image-292-%C3%97-292-pixels.jpeg"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/06/itunesart.jpg"},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/10/480x270_201238-150x150.jpg"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2018/11/fromembers.jpg"},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2019/03/Large-1-1024x1024.jpg"},
        {
            'label': plugin.get_string(30021),
            'path': plugin.url_for('episodes21'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2019/07/shit-2-150x150.png"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(url12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(url13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(url14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(url15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(url16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(url17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(url18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(url19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(url20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items
@plugin.route('/episodes21/')
def episodes21():
    soup21 = mainaddon.get_soup21(url21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
if __name__ == '__main__':
    plugin.run()
