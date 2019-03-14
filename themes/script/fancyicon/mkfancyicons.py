import os
import shutil

"""
百变主题 辅助生成工具
"""


# 纯汉字 检查
# 检验是否含有中文字符
def isContainChinese(s):
    for c in s:
        if ('\u4e00' <= c <= '\u9fa5'):
            return True
    return False


# 检验是否全是中文字符
def is_all_chinese(s):
    for c in s:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


# 全是英文
def is_english(msg):
    is_english_str = False
    for uchar in msg:
        """判断一个unicode是否是英文字母"""
        if (u'\u0041' <= uchar <= u'\u005a') or (u'\u0061' <= uchar <= u'\u007a'):
            is_english_str = True
        else:
            is_english_str = False
            break
    return is_english_str


def write_single_row(f_name, app_icon_text):
    with open('single_row.xml', 'r') as f:
        manifest_text = f.read().replace('name', app_icon_text.lower())
        # print("保存配置文件……")
        file = open(f_name, 'w+', encoding='utf-8')
        file.write(manifest_text)
        file.close()


def write_double_row(f_name, first_line_name, second_line_name):
    with open('double_row.xml', 'r') as f:
        manifest_text = f.read().replace('name1', first_line_name).replace('name2', second_line_name)
        # print("保存配置文件……")
        file = open(f_name, 'w+', encoding='utf-8')
        file.write(manifest_text)
        file.close()


if __name__ == '__main__':
    # 百变主题的根目录
    dir_fancy_icons = "fancy_icons/"
    # 百变主题背景icon所在路径
    dir_icon_background = "transparent.png"
    app_map = {'浏览器': 'com.android.browser',
               '日历': 'com.android.calendar',
               '相机': 'com.android.camera',
               '联系人': 'com.android.contacts',
               '电话': 'com.android.contacts',
               '时钟': 'com.android.deskclock',
               '电子邮件': 'com.android.email',
               '文件管理': 'com.android.fileexplorer',
               '短信': 'com.android.mms',
               '设置': 'com.android.settings',
               '个性主题': 'com.android.thememanager',
               '小米钱包': 'com.mipay.wallet',
               '计算器': 'com.miui.calculator',
               '相册': 'com.miui.gallery',
               '便签': 'com.miui.notes',
               '天气': 'com.miui.weather2',
               '应用商店': 'com.xiaomi.market',
               '扫一扫': 'com.xiaomi.scanner',
               '酷我音乐': 'cn.kuwo.player',
               '最右': 'cn.xiaochuankeji.tieba',
               '币快报': 'com.link.beenews',
               '英语流利说': 'com.liulishuo.engzo',
               '爱壁纸': 'com.lovebizhi.wallpaper',
               ' 360手机助手': 'com.qihoo.appstore',
               '小米贷款': 'com.xiaomi.loan',
               '网易有道词典': 'com.youdao.dict',
               '饿了么': 'me.ele',
               '下载管理': 'com.android.providers.downloads.ui',
               '录音机': 'com.android.soundrecorder',
               'USIM卡应用': 'com.android.stk',
               '用户反馈': 'com.miui.bugreport',
               '指南针': 'com.miui.compass',
               '音乐': 'com.miui.player',
               '屏幕录制': 'com.miui.screenrecorder',
               '安全中心': 'com.miui.securitycenter',
               '小米视频': 'com.miui.video',
               '全球上网': 'com.miui.virtualsim',
               '小爱同学': 'com.miui.voiceassist',
               '游戏中心': 'com.xiaomi.gamecenter',
               '我的小米': 'com.xiaomi.vipaccount',
               '招商银行': 'cmb.pb',
               '慕课网': 'cn.com.open.mooc',
               '新华字典': 'cn.dictcn.android.digitize.swg_xhzd_21003',
               '个人所得税': 'cn.gov.tax.its',
               '车友头条': 'cn.mucang.android.qichetoutiao',
               'WPS Office': 'cn.wps.moffice_eng',
               '皮皮搞笑': 'cn.xiaochuankeji.zuiyouLite',
               '铁路12306': 'com.MobileTicket',
               'UC浏览器': 'com.UCMobile',
               '中国农业银行': 'com.android.bankabc',
               'Metro大都会': 'com.app.shanghai.metro',
               '高德地图': 'com.autonavi.minimap',
               '小学语文同步辅导': 'com.babybar.primchinese',
               '百词斩爱阅读': 'com.baicizhan.ireading',
               '百度网盘': 'com.baidu.netdisk',
               '聚合新闻': 'com.binny.openapi',
               '多开分身': 'com.bly.dkplat',
               '菜鸟裹裹': 'com.cainiao.wireless',
               '中华会计网校': 'com.cdel.accmobile',
               '唱吧': 'com.changba',
               '中国建设银行': 'com.chinamworld.main',
               '和飞信': 'com.chinasofti.rcs',
               '掌上生活': 'com.cmbchina.ccd.pluto.cmbActivity',
               '电信营业厅': 'com.ct.client',
               '掘金': 'com.daimajia.gold',
               '大众点评': 'com.dianping.v1',
               '万能遥控': 'com.duokan.phone.remotecontroller',
               '阅读': 'com.duokan.reader',
               '虎牙直播': 'com.duowan.kiwi',
               '支付宝': 'com.eg.android.AlipayGphone',
               '考研万题库': 'com.exam8.KYzhengzhi',
               '福昕PDF阅读器': 'com.foxit.mobile.pdf.lite',
               'Keep': 'com.gotokeep.keep',
               '驾考宝典': 'com.handsgo.jiakao.android',
               'Boss直聘': 'com.hpbr.bosszhipin',
               '虎扑': 'com.hupu.games',
               '中国工商银行': 'com.icbc',
               '考研英语': 'com.ikaoshi.english.kaoyanreading',
               '考研政治题库宝典': 'com.ikaoshi.kaoyan.politics',
               '小学语文': 'com.itfirer.primaryschoolchinese',
               '京东金融': 'com.jd.jrapp',
               '简书': 'com.jianshu.haruki',
               '世纪佳缘': 'com.jiayuan',
               '京东': 'com.jingdong.app.mall',
               '百词斩': 'com.jiongji.andriod.card',
               '前程无忧51job': 'com.job.android',
               '表情广场': 'com.kk.biaoqing',
               '古诗词典': 'com.kk.poem',
               'Vysor': 'com.koushikdutta.vysor',
               '酷狗音乐': 'com.kugou.android',
               '来分期': 'com.laifenqi.android.app',
               '乐学高考': 'com.lexue.courser',
               '贝壳找房': 'com.lianjia.beike',
               '高中知识点大全': 'com.ljy.gzzsddq',
               '得到': 'com.luojilab.player',
               '摩拜单车': 'com.mobike.mobikeapp',
               '高考化学通': 'com.moyun365.android.gkchemistrytong',
               '网商银行': 'com.mybank.android.phone',
               'ZAKER新闻': 'com.myzaker.ZAKER_Phone',
               '网易邮箱': 'com.netease.mobimail',
               '花生地铁': 'com.nfyg.hsbb',
               '物理大师-初高中版': 'com.physicmaster',
               '平安金管家': 'com.pingan.lifeinsurance',
               '平安口袋银行': 'com.pingan.paces.ccms',
               '爱奇艺': 'com.qiyi.video',
               'QQ空间': 'com.qzone',
               '即刻': 'com.ruguoapp.jike',
               '美团': 'com.sankuai.meituan',
               '名人朋友圈': 'com.sencent.mm',
               '微博': 'com.sina.weibo',
               '手机营业厅': 'com.sinovatech.unicom.ui',
               '今日头条': 'com.ss.android.article.news',
               '抖音短视频': 'com.ss.android.ugc.aweme',
               '考研帮': 'com.tal.kaoyan',
               '闲鱼': 'com.taobao.idlefish',
               '手机淘宝': 'com.taobao.taobao',
               '飞猪': 'com.taobao.trip',
               '脉脉': 'com.taou.maimai',
               'QQ邮箱': 'com.tencent.androidqqmail',
               '微信': 'com.tencent.mm',
               'QQ': 'com.tencent.mobileqq',
               '腾讯视频': 'com.tencent.qqlive',
               'QQ同步助手': 'com.tencent.qqpim',
               '掌上英雄联盟': 'com.tencent.qt.qtl',
               'QQ影音': 'com.tencent.research.drop',
               '绝地求生 刺激战场': 'com.tencent.tmgp.pubgmhd',
               '王者荣耀': 'com.tencent.tmgp.sgame',
               'QQ安全中心': 'com.tencent.token',
               '微信读书': 'com.tencent.weread',
               '企业微信': 'com.tencent.wework',
               '天眼查企业查询': 'com.tianyancha.skyeye',
               '云闪付': 'com.unionpay',
               '下厨房': 'com.xiachufang',
               '高中语文': 'com.xiangqi.gzchinese',
               '小米社区': 'com.xiaomi.bbslite',
               '小爱音箱': 'com.xiaomi.mico',
               '小米省钱购': 'com.xiaomi.o2o',
               '小米商城': 'com.xiaomi.shop',
               '喜马拉雅': 'com.ximalaya.ting.android',
               '高中数学': 'com.xlink.gaozhongshuxuebibei',
               '高中物理知识大全': 'com.xlink.gaozhongwulizhishidaquan',
               '拼多多': 'com.xunmeng.pinduoduo',
               '优酷视频': 'com.youku.phone',
               '考研派': 'com.yuekao.kaoyanquestion',
               '高考蜂背': 'com.zhouyue.Bee',
               '招联金融': 'com.zl.fqbao',
               '携程旅行': 'ctrip.android.view',
               '企业微信分身': 'dkplugin.lse.ptf',
               '虾米音乐': 'fm.xiami.main',
               'imToken': 'im.token.app',
               '多闪': 'my.maya.android',
               '二年级语文下册': 'org.cocos2dx.yuwenbubian3014',
               '小学语文五年级下': 'org.cocos2dx.yuwenbubian3018',
               '小学语文四年级下': 'org.cocos2dx.yuwenbubian3020',
               'IONC Token': 'org.ionchain.wallet',
               '肖秀荣政治': 'xxrzz.hskaoyan'
               }

    for key, value in app_map.items():
        # print(key + ":" + value)

        # 拼接一个新文件夹的路径
        icon_pkg_name_folder_path = os.path.join(dir_fancy_icons, value)

        # print("即将创建的文件夹的路径=" + os.path.join(dir_fancy_icons, value))

        """
        判断是不是日历和天气
        如果是，跳过读写

        """

        # 创建百变图标的文件目录
        """
        1   判断文件是否存在
            文件夹不存在，则创建文件夹
        """
        if key == "日历" or key == "天气":
            print("跳过 ：" + key)
            continue
        if not os.path.exists(icon_pkg_name_folder_path):
            # 创建一个新目录
            os.makedirs(icon_pkg_name_folder_path)
        # print("文件夹已存在：" + icon_pkg_name_folder_path)
        # 创建完成之后，拷贝背景icon
        """
        2   判断背景图标是否存在，不存在则拷贝过去
        """
        icon_bg_path = os.path.join(icon_pkg_name_folder_path, "bg.png")
        print(icon_bg_path)
        if not os.path.exists(icon_bg_path):
            shutil.copyfile(dir_icon_background, icon_pkg_name_folder_path + "/bg.png")
        # print("背景图标存在")

        # 文件读写
        # 纯汉字
        file_name = os.path.join(icon_pkg_name_folder_path, "manifest.xml")
        # print(key+"  "+str(len(key)))
        key = key.replace(' ', '')
        count = len(key)
        if count <= 3 or is_english(key):  # 单行，居中模板
            # print(key)
            write_single_row(file_name, key)
        elif count == 4:  # 双行，居中 王者荣耀
            first_name = key[0:2]  # 王者
            second_name = key[2:4]  # 荣耀
            # print(first_name)
            # print(second_name)
            write_double_row(file_name, first_name, second_name)
            # print("保存配置文件……Done!")
        elif count == 5:  # 双行，居中 王者荣耀啊
            first_name = key[0:2]  # 王者
            second_name = key[2:5]  # 荣耀啊
            # print(first_name)
            # print(second_name)
            if key.isdecimal():
                write_single_row(file_name, key)
            else:
                write_double_row(file_name, first_name, second_name)
                # print("保存配置文件……Done!")
        elif count == 6:  # 双行，居中 王者荣耀啊
            first_name = key[0:3]  # 王者
            second_name = key[3:6]  # 荣耀啊
            write_double_row(file_name, first_name, second_name)
        elif count == 7:
            index = int(len(key) / 2 + 1)
            first_name = key[0:index]  # 王者
            second_name = key[index:len(key)]  # 荣耀啊
            write_double_row(file_name, first_name, second_name)
        elif count == 8:
            index = int(len(key) / 2)
            first_name = key[0:index]  # 王者
            second_name = key[index:len(key)]  # 荣耀啊
            write_double_row(file_name, first_name, second_name)
