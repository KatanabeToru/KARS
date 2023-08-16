##################
## SW 测试 画图  ##
##################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
import math

####################################   数据集 DouBanDatasets_SWTest   #################################

###########################  RMSE    DouBanDatasets_SWTest ###########################
# fig = plt.figure()
#
# # 去掉前w_i小的规模，也就是数据集规模从大到小
# DataClippingScale = [0,0.05,0.1,0.15,0.2,0.25,.3,0.35,0.4,0.45,0.5]
#
# Douban_RMSE_HARS = [0.9536485975293897,0.9506970041452463,0.94612203047051,0.9433789589455827,0.9332342311714844,0.9328410911174998,0.9281822593924229,0.9269895661897101,0.9163081456709807,0.9122507504415833,0.913773247840233]
# Douban_RMSE_KDEm = [1.0884593133702398, 1.0834046573882943, 1.0866304329548937, 1.0686018291205095, 1.0392865265492455, 1.007346671951424, 1.0078253606346277, 1.0162979102191099, 1.0161808027103336, 1.0203619661454488, 1.0564076292430913]
# Douban_RMSE_CATD  = [1.0500652547446507, 1.0400312229056239, 1.0345162323883277, 1.0344261949706737, 1.032627339962152, 1.0252750806499051, 1.0195320110206287, 1.0180537715362297, 1.0221989202065873, 1.0167649613574972, 1.0123508245134194]
# Douban_RMSE_CRH  = [0.9778002406099365, 0.9702301403774091, 0.9630610621327749, 0.9561695031964911, 0.9505448800899713, 0.9405441389619035, 0.9341223634415055, 0.9339092761688189, 0.9322869242758356, 0.9214816419849489, 0.9252446413006988]
# Douban_RMSE_GTM  = [0.8290786297710278, 0.8238871718625634, 0.8233605684530486, 0.8353874786138582, 0.8303830801789678, 0.8287183193394628, 0.8473980938683806, 0.86886864302825, 0.9152237124526764, 0.9587643367859706, 0.9864193218002031]
# Douban_RMSE_LFCN = [1.1788688267995253, 1.15163604403709, 1.1305438737022981, 1.1118131903729935, 1.094004459825462, 1.0789076060287848, 1.062831194470258, 1.055252904637246, 1.0449912810368704, 1.0322103004074, 1.022195781922726]
#
#
# ## 画 真实指标
# plt.plot(DataClippingScale,Douban_RMSE_HARS, marker = 'o',color = 'r', label = 'HARS')
# plt.plot(DataClippingScale,Douban_RMSE_KDEm, marker = '^',color = 'fuchsia', label = 'KDEm')
# plt.plot(DataClippingScale,Douban_RMSE_CATD, marker = 's',color = 'deepskyblue', label = 'CATD')
# plt.plot(DataClippingScale,Douban_RMSE_CRH,  marker = '.',color = 'gray', label = 'CRH')
# plt.plot(DataClippingScale,Douban_RMSE_GTM,marker = 'D',color = 'gold', label = 'GTM')
# plt.plot(DataClippingScale,Douban_RMSE_LFCN, marker = 'v',color = 'g', label = 'LFC_N')
#
# plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# plt.gca().spines["top"].set_alpha(0.3)
# plt.gca().spines["right"].set_alpha(0.3)
# plt.gca().spines["bottom"].set_alpha(0.3)
# plt.gca().spines["left"].set_alpha(0.3)
# plt.xticks(fontsize=12, alpha=0.7)
# plt.yticks(fontsize=12, alpha=0.7)
# plt.xticks(np.arange(0,0.55,0.05))
# plt.xlabel("Data Clipping Scale",fontsize = 15)
# plt.ylabel("RMSE",fontsize = 15)
# plt.title("DouBanDatasets_SW_Test",fontsize = 20)
# plt.legend(loc='upper right',bbox_to_anchor=(1, 1.02))
#
# plt.savefig('C:/Users/chopin/Desktop/'+'SW_Douban_RMSE.pdf', bbox_inches='tight')
#
# plt.show()
#
#
# ###########################  MAE   DouBanDatasets_SWTest ###########################
#
# fig = plt.figure()
#
# # 去掉前w_i小的规模，也就是数据集规模从大到小
# DataClippingScale = [0,0.05,0.1,0.15,0.2,0.25,.3,0.35,0.4,0.45,0.5]
#
# Douban_MAE_HARS = [0.7584816396279375,0.7544836454692834,0.7506769220446602,0.7485691553153987,0.7402168849094828,0.7400406226137363,0.7370760867552963,0.7366655791366584,0.7256815582018254,0.7236362144766503,0.7256642497078273]
# Douban_MAE_KDEm  = [0.8555869093659136, 0.8550063423941837, 0.8645222761060335, 0.8482165596189026, 0.8206202201185739, 0.8145348041041578, 0.8175073827268401, 0.8201029731746012, 0.8003990401876181, 0.7889209811382345, 0.8151892598287038]
# Douban_MAE_CATD  = [0.8504133785641106, 0.8416603973055243, 0.8376914150056202, 0.8384124470405435, 0.8369860073125986, 0.8283196981101107, 0.8211136057987354, 0.8194622395809846, 0.8260819040170209, 0.8216350643900833, 0.8175513457039714]
# Douban_MAE_CRH  = [0.7915831817213516, 0.785469470373691, 0.7794670827017524, 0.7733117746048707, 0.7641096632311087, 0.7549168481960156, 0.749007876797308, 0.7459628773271526, 0.743095331333975, 0.7329410361811158, 0.7373101092487889]
# Douban_MAE_GTM = [0.6626100054823264, 0.6594378886437522, 0.6617869584271978, 0.6713588970888872, 0.6577368572608681, 0.66591015101181, 0.6778261500019276, 0.6855577403383163, 0.7430133431182543, 0.7720147270103082, 0.7904812492164017]
# Douban_MAE_LFCN  = [0.9821569008599518, 0.953688058849431, 0.9320602391984927, 0.9123291952037623, 0.8940689444578976, 0.8775270984177135, 0.8609395974927919, 0.8529175737646725, 0.8428405953243717, 0.830084840235255, 0.8205292815427242]
#
# Douban_MAE_CTD = []
#
# # # 对数化指标
# # Log_Douban_MAE_HARS = []
# # Log_Douban_MAE_KDEm = []
# # Log_Douban_MAE_CATD = []
# # Log_Douban_MAE_CRH = []
# # Log_Douban_MAE_GTM = []
# # Log_Douban_MAE_LFCN = []
# # Log_Douban_MAE_CTD = []
# # for val in Douban_MAE_HARS:
# #     Log_Douban_MAE_HARS.append(math.log(val))
# # for val in Douban_MAE_KDEm:
# #     Log_Douban_MAE_KDEm.append(math.log(val))
# # for val in Douban_MAE_CATD:
# #     Log_Douban_MAE_CATD.append(math.log(val))
# # for val in Douban_MAE_CRH:
# #     Log_Douban_MAE_CRH.append(math.log(val))
# # for val in Douban_MAE_GTM:
# #     Log_Douban_MAE_GTM.append(math.log(val))
# # for val in Douban_MAE_LFCN:
# #     Log_Douban_MAE_LFCN.append(math.log(val))
# # for val in Douban_MAE_CTD:
# #     Log_Douban_MAE_CTD.append(math.log(val))
#
#
#
# ## 画 真实指标
# plt.plot(DataClippingScale,Douban_MAE_HARS, marker = 'o',color = 'r', label = 'HARS')
# plt.plot(DataClippingScale,Douban_MAE_KDEm, marker = '^',color = 'fuchsia', label = 'KDEm')
# plt.plot(DataClippingScale,Douban_MAE_CATD, marker = 's',color = 'deepskyblue', label = 'CATD')
# plt.plot(DataClippingScale,Douban_MAE_CRH,  marker = '.',color = 'gray', label = 'CRH')
# plt.plot(DataClippingScale,Douban_MAE_GTM,marker = 'D',color = 'gold', label = 'GTM')
# plt.plot(DataClippingScale,Douban_MAE_LFCN, marker = 'v',color = 'g', label = 'LFC_N')
# # plt.plot(DataClippingScale,Douban_MAE_CTD,marker = 'p',color = 'peru', label = 'CTD')
#
#
# ##  画 对数化指标
# # plt.plot(DatasetSize,Log_Douban_MAE_HARS,marker = 'o',color = 'r', label = 'HARS')
# # plt.plot(DatasetSize,Log_Douban_MAE_KDEm,marker = '^',color = 'fuchsia', label = 'KDEm')
# # plt.plot(DatasetSize,Log_Douban_MAE_CATD,marker = 's',color = 'deepskyblue', label = 'CATD')
# # plt.plot(DatasetSize,Log_Douban_MAE_CRH, marker = '.',color = 'gray', label = 'CRH')
# # plt.plot(DatasetSize,Log_Douban_MAE_GTM, marker = 'D',color = 'gold', label = 'GTM')
# # plt.plot(DatasetSize,Log_Douban_MAE_LFCN,marker = 'v',color = 'g', label = 'LFC_N')
# # plt.plot(DatasetSize,Log_Douban_MAE_CTD,marker = 'p',color = 'peru', label = 'CTD')
#
# plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# plt.gca().spines["top"].set_alpha(0.3)
# plt.gca().spines["right"].set_alpha(0.3)
# plt.gca().spines["bottom"].set_alpha(0.3)
# plt.gca().spines["left"].set_alpha(0.3)
# plt.xticks(fontsize=12, alpha=0.7)
# plt.yticks(fontsize=12, alpha=0.7)
# plt.xticks(np.arange(0,0.55,0.05))
# plt.xlabel("Data Clipping Scale",fontsize = 15)
# plt.ylabel("MAE",fontsize = 15)
# plt.title("DouBanDatasets_SW_Test",fontsize = 20)
#
# plt.legend()
#
# plt.savefig('C:/Users/chopin/Desktop/'+'SW_Douban_MAE.pdf', bbox_inches='tight')
#
# plt.show()





####################################   数据集 GoodReadsDatasets_SWTest   #################################

##########################  RMSE  GoodReadsDatasets_SWTest  ############################
#
# fig = plt.figure()
#
# # 去掉前w_i小的规模，也就是数据集规模从大到小
# DataClippingScale = [0,0.05,0.1,0.15,0.2,0.25,.3,0.35,0.4,0.45,0.5]
# ## SWTest1
# # GoodReads_RMSE_HARS =  [0.49920386943591943, 0.4996812212906693, 0.5052390845084593, 0.5304021319759081, 0.5212586852373591, 0.5329933877221498, 0.5284080071406557, 0.535460700716291, 0.5282549003704193, 0.5272072894786226, 0.4971007676295575]
#
# ## SWTest2
# # GoodReads_RMSE_HARS = [0.39692544765371907,0.40055922269328176,0.4096394931971623,0.4100761082276455,0.4168186671505892,0.415642180108293,0.4162364949329691,0.42194164638331516,0.42,0.42,0.42]
# # GoodReads_RMSE_KDEm  = [0.663508929688802, 0.6788285268585008, 0.6832802105907471, 0.6971677445075464, 0.6797615285552139, 0.689868436489732, 0.6567972037043184, 0.6862155863476426, 0.7102396826396575, 0.6926083015171949, 0.7019449766067898]
# # GoodReads_RMSE_CATD  = [0.528209530222583, 0.5351087505926799, 0.5427539794169692, 0.5790686279083793, 0.5779227835869221, 0.5774075516309, 0.5822567564552601, 0.5943861721777657, 0.5973458175424177, 0.6292813126364188, 0.613213593464857]
# # GoodReads_RMSE_CRH  = [0.5013133477357062, 0.5082144562179481, 0.5157586187157938, 0.5373112651765782, 0.5314236724505623, 0.5418495115973879, 0.5436088974848109, 0.553053509889849, 0.5559572626099945, 0.5502983192407903, 0.5169873488155812]
# # GoodReads_RMSE_GTM  = [1.8078018803924962, 1.8580821481076957, 1.9043318612358011, 1.9578111569093013, 2.0005656094948088, 2.0583399568450553, 2.099976093729745, 2.1625446203909933, 2.2246631200926883, 2.3036830883981474, 2.3756502577333816]
# # GoodReads_RMSE_LFCN  = [0.4472208331280819, 0.4519472731266155, 0.45857778871103494, 0.49023633374339104, 0.4819645283731126, 0.487891773497424, 0.48350149698322503, 0.4907071544830689, 0.5004329471427187, 0.4959941588640746, 0.46749413492321495]
#
# ## SWTest3
# GoodReads_RMSE_HARS =  [0.4020628704954403, 0.40138553371688146, 0.40714430775817784, 0.408705443189294, 0.41172851554074147, 0.41467228397858014, 0.41480390471615947, 0.4204580551904548, 0.4237592358365512, 0.42550160491657835, 0.4207209784745644]
# GoodReads_RMSE_KDEm  = [0.6261600187654166, 0.6371011726290755, 0.6413429964614294, 0.6292366790594298, 0.6196442113202767, 0.6149887377524555, 0.5803537937760951, 0.6018859733737119, 0.6226607251646781, 0.6070538256176868, 0.6341171656493197]
# GoodReads_RMSE_CATD  = [0.41986015808006355, 0.4228875522870503, 0.435099848179513, 0.4336614695025245, 0.43907584273325606, 0.4400118189056, 0.4435397395391241, 0.4539484216293331, 0.4620403813711352, 0.49012799064606827, 0.5025678413986684]
# GoodReads_RMSE_CRH  = [0.3891124992447327, 0.3944668578902128, 0.39898650916143313, 0.401320238824459, 0.4042905023326872, 0.411491529613789, 0.41450921832392273, 0.4184689577117371, 0.4226122706835486, 0.4206947735438018, 0.4227149593225956]
# GoodReads_RMSE_GTM  = [1.7583966674557088, 1.8093635752698496, 1.854774542538247, 1.8992614686789704, 1.943791560887706, 1.9927029482218026, 2.0528669783164584, 2.116551984580622, 2.1728497993700073, 2.2610530642374362, 2.3426009436276294]
# GoodReads_RMSE_LFCN  = [0.3253822562495753, 0.32896615951350977, 0.3313234878730418, 0.3320477474457253, 0.3335834065135065, 0.3369275122876941, 0.3368370053113285, 0.33638056474523287, 0.34284350884578574, 0.34768807401329244, 0.35473037080127334]
#
#
# # 对数化指标
# Log_GoodReads_RMSE_HARS = []
# Log_GoodReads_RMSE_KDEm = []
# Log_GoodReads_RMSE_CATD = []
# Log_GoodReads_RMSE_CRH = []
# Log_GoodReads_RMSE_GTM = []
# Log_GoodReads_RMSE_LFCN = []
#
# for val in GoodReads_RMSE_HARS:
#     Log_GoodReads_RMSE_HARS.append(math.log(val))
# for val in GoodReads_RMSE_KDEm:
#     Log_GoodReads_RMSE_KDEm.append(math.log(val))
# for val in GoodReads_RMSE_CATD:
#     Log_GoodReads_RMSE_CATD.append(math.log(val))
# for val in GoodReads_RMSE_CRH:
#     Log_GoodReads_RMSE_CRH.append(math.log(val))
# for val in GoodReads_RMSE_GTM:
#     Log_GoodReads_RMSE_GTM.append(math.log(val))
# for val in GoodReads_RMSE_LFCN:
#     Log_GoodReads_RMSE_LFCN.append(math.log(val))
#
#
# ## 画 真实指标
# # plt.plot(DataClippingScale,GoodReads_RMSE_HARS, marker = 'o',color = 'r', label = 'HARS')
# # plt.plot(DataClippingScale,GoodReads_RMSE_KDEm, marker = '^',color = 'fuchsia', label = 'KDEm')
# # plt.plot(DataClippingScale,GoodReads_RMSE_CATD, marker = 's',color = 'deepskyblue', label = 'CATD')
# # plt.plot(DataClippingScale,GoodReads_RMSE_CRH,  marker = '.',color = 'gray', label = 'CRH')
# # plt.plot(DataClippingScale,GoodReads_RMSE_GTM,marker = 'D',color = 'gold', label = 'GTM')
# # plt.plot(DataClippingScale,GoodReads_RMSE_LFCN, marker = 'v',color = 'g', label = 'LFC_N')
#
# #  画 对数化指标
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_HARS,marker = 'o',color = 'r', label = 'HARS')
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_KDEm,marker = '^',color = 'fuchsia', label = 'KDEm')
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_CATD,marker = 's',color = 'deepskyblue', label = 'CATD')
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_CRH, marker = '.',color = 'gray', label = 'CRH')
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_GTM, marker = 'D',color = 'gold', label = 'GTM')
# plt.plot(DataClippingScale,Log_GoodReads_RMSE_LFCN,marker = 'v',color = 'g', label = 'LFC_N')
#
#
#
# plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# plt.gca().spines["top"].set_alpha(0.3)
# plt.gca().spines["right"].set_alpha(0.3)
# plt.gca().spines["bottom"].set_alpha(0.3)
# plt.gca().spines["left"].set_alpha(0.3)
# plt.xticks(fontsize=12, alpha=0.7)
# plt.yticks(fontsize=12, alpha=0.7)
# plt.xticks(np.arange(0,0.55,0.05))
# plt.xlabel("Data Clipping Scale",fontsize = 15)
# plt.ylabel("Log(RMSE)",fontsize = 15)
# plt.title("GoodReadsDatasets_SW_Test",fontsize = 20)
# plt.legend(loc='center right',bbox_to_anchor=(1, 0.6))
#
# plt.savefig('C:/Users/chopin/Desktop/'+'SW_GoodReads_RMSE.pdf', bbox_inches='tight')
#
# plt.show()
#
#
#
#
# ##########################  MAE  GoodReadsDatasets_SWTest  ############################
#
# fig = plt.figure()
#
# # 去掉前w_i小的规模，也就是数据集规模从大到小
# DataClippingScale = [0,0.05,0.1,0.15,0.2,0.25,.3,0.35,0.4,0.45,0.5]
#
# ## SWTest1
# # GoodReads_MAE_HARS = [0.31850767661673124,0.32218445302358767,0.3306651269841593,0.3338136444953708,0.3430491843317213,0.33990968400747373,0.34080304662833383,0.3472239282512779,0.34,0.34,0.34]
#
# # ## SWTest2
# # GoodReads_MAE_HARS =  [0.4064966434100951, 0.40556743753412544, 0.41059261171111977, 0.42846772966777197, 0.4237167486041848, 0.43091159546781227, 0.4267426057398194, 0.432882645402052, 0.435813966976569, 0.43380739269410795, 0.40710972940340456]
# # GoodReads_MAE_KDEm  = [0.46681477844541935, 0.48812015672343356, 0.49187425252358846, 0.5124849668265531, 0.5095506234747961, 0.5106938904694391, 0.4929321508527051, 0.5105062952371139, 0.5356826003566443, 0.5329218703911317, 0.5073479409220576]
# # GoodReads_MAE_CATD  = [0.4026231675938866, 0.4097571032452818, 0.4151980394103386, 0.4470341815749228, 0.44877045331983373, 0.4569295516695828, 0.45634368227136224, 0.45950208983877977, 0.4640408414981081, 0.47610535823670735, 0.47866059636532426]
# # GoodReads_MAE_CRH  = [0.4047298765003982, 0.41160245754636365, 0.4151974469670438, 0.43872344208471753, 0.4299051427208836, 0.4358595522999326, 0.43496012831363207, 0.44470741456014234, 0.4499712977278692, 0.44540169753299924, 0.4219886970677332]
# # GoodReads_MAE_GTM  = [1.4806958947123927, 1.5310167743716505, 1.5782119195516051, 1.6338477163145373, 1.6775027377616172, 1.729616624125559, 1.7845616311416328, 1.8532905362460927, 1.9215293979961294, 2.0120466222212365, 2.1040011921326913]
# # GoodReads_MAE_LFCN  = [0.3496348818781699, 0.35299839114720916, 0.35515401138826164, 0.3835951227965735, 0.3809169532628076, 0.3868555498025401, 0.38285469363621377, 0.3858530277648879, 0.3977617678328793, 0.39629952667763596, 0.37465573150197307]
#
# # SWTest3
# GoodReads_MAE_HARS =  [0.3251809551754977, 0.32438124819554254, 0.3305566046465743, 0.3347358080543372, 0.3366399408599069, 0.34005962992699745, 0.34084319678415714, 0.34736190746696954, 0.3488510819447298, 0.35285496023425983, 0.3467127200292093]
# GoodReads_MAE_KDEm  = [0.40860861646284824, 0.42136319507592335, 0.4251651328921978, 0.4154667383924846, 0.4120257923071995, 0.40936742328465725, 0.3997395804645619, 0.4106710311459755, 0.4304084768904047, 0.4271131984548107, 0.4409926463466585]
# GoodReads_MAE_CATD  = [0.30980024766151126, 0.312779894472333, 0.3235784215189286, 0.32682942721245545, 0.3325751674720699, 0.3339584277902703, 0.3371186455908656, 0.3461292941263188, 0.351826685522894, 0.3669144953757077, 0.3752608508557026]
# GoodReads_MAE_CRH  = [0.3086734744677913, 0.3158218932735356, 0.3199825360122097, 0.32339847562739643, 0.326219522348021, 0.33130013705740197, 0.3334643203430194, 0.33560352521899356, 0.33981866044935793, 0.33977764434724145, 0.3395380687567131]
# GoodReads_MAE_GTM  = [1.4679972177327234, 1.519560088633236, 1.567832281152731, 1.617516560941035, 1.6674689536295448, 1.7209684301475572, 1.7844254271833528, 1.8527050518174257, 1.920182087389805, 2.01172194689656, 2.103676516808017]
# GoodReads_MAE_LFCN  = [0.24610255650395796, 0.24907722027423992, 0.2514313965469607, 0.2515432893434424, 0.2540678447145513, 0.2575924300197741, 0.2597154025204378, 0.2594879130264167, 0.2652878105014751, 0.2702499863156088, 0.2748597457631456]
#
#
# # 对数化指标
# Log_GoodReads_MAE_HARS = []
# Log_GoodReads_MAE_KDEm = []
# Log_GoodReads_MAE_CATD = []
# Log_GoodReads_MAE_CRH = []
# Log_GoodReads_MAE_GTM = []
# Log_GoodReads_MAE_LFCN = []
# for val in GoodReads_MAE_HARS:
#     Log_GoodReads_MAE_HARS.append(math.log(val))
# for val in GoodReads_MAE_KDEm:
#     Log_GoodReads_MAE_KDEm.append(math.log(val))
# for val in GoodReads_MAE_CATD:
#     Log_GoodReads_MAE_CATD.append(math.log(val))
# for val in GoodReads_MAE_CRH:
#     Log_GoodReads_MAE_CRH.append(math.log(val))
# for val in GoodReads_MAE_GTM:
#     Log_GoodReads_MAE_GTM.append(math.log(val))
# for val in GoodReads_MAE_LFCN:
#     Log_GoodReads_MAE_LFCN.append(math.log(val))
#
#
# # ## 画 真实指标
# # plt.plot(DataClippingScale,GoodReads_MAE_HARS, marker = 'o',color = 'r', label = 'HARS')
# # plt.plot(DataClippingScale,GoodReads_MAE_KDEm, marker = '^',color = 'fuchsia', label = 'KDEm')
# # plt.plot(DataClippingScale,GoodReads_MAE_CATD, marker = 's',color = 'deepskyblue', label = 'CATD')
# # plt.plot(DataClippingScale,GoodReads_MAE_CRH,  marker = '.',color = 'gray', label = 'CRH')
# # plt.plot(DataClippingScale,GoodReads_MAE_GTM,marker = 'D',color = 'gold', label = 'GTM')
# # plt.plot(DataClippingScale,GoodReads_MAE_LFCN, marker = 'v',color = 'g', label = 'LFC_N')
#
# #  画 对数化指标
# plt.plot(DataClippingScale,Log_GoodReads_MAE_HARS,marker = 'o',color = 'r', label = 'HARS')
# plt.plot(DataClippingScale,Log_GoodReads_MAE_KDEm,marker = '^',color = 'fuchsia', label = 'KDEm')
# plt.plot(DataClippingScale,Log_GoodReads_MAE_CATD,marker = 's',color = 'deepskyblue', label = 'CATD')
# plt.plot(DataClippingScale,Log_GoodReads_MAE_CRH, marker = '.',color = 'gray', label = 'CRH')
# plt.plot(DataClippingScale,Log_GoodReads_MAE_GTM, marker = 'D',color = 'gold', label = 'GTM')
# plt.plot(DataClippingScale,Log_GoodReads_MAE_LFCN,marker = 'v',color = 'g', label = 'LFC_N')
#
#
# plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# plt.gca().spines["top"].set_alpha(0.3)
# plt.gca().spines["right"].set_alpha(0.3)
# plt.gca().spines["bottom"].set_alpha(0.3)
# plt.gca().spines["left"].set_alpha(0.3)
# plt.xticks(fontsize=12, alpha=0.7)
# plt.yticks(fontsize=12, alpha=0.7)
# plt.xticks(np.arange(0,0.55,0.05))
# plt.xlabel("Data Clipping Scale",fontsize = 15)
# plt.ylabel("Log(MAE)",fontsize = 15)
# plt.title("GoodReadsDatasets_SW_Test",fontsize = 20)
# plt.legend(loc='center right',bbox_to_anchor=(1, 0.6))
#
# plt.savefig('C:/Users/chopin/Desktop/'+'SW_GoodReads_MAE.pdf', bbox_inches='tight')
#
# plt.show()


#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################



###############################  两个数据集画一张图上  ##########################################
DataClippingScale = [0,0.05,0.1,0.15,0.2,0.25,.3,0.35,0.4,0.45,0.5]
Douban_RMSE_HARS =  [0.9549024787895418,0.949014157871162,0.9444667233384225,0.9411886644343485,0.9319225402593098,0.9280813927301313,0.9238979301235463,0.9210864737708325,0.9160688700233759,0.9079389320953095,0.9083231779606425]
Douban_MAE_HARS =  [0.7574701683414208,0.7516614450006354,0.7491603526689402,0.7465377691537911,0.7381292168001409,0.7346272286056329,0.7313213118324855, 0.7284021735554137,0.7239129176001797,0.716038145913582,0.7194054584116987]
GoodReads_RMSE_HARS =  [0.40338203631556063, 0.4038697484247689, 0.40748551008459044, 0.4080572894818407, 0.41365923151225575, 0.41840602055197057, 0.4152086982641798, 0.41946050424241754, 0.4240696091718623, 0.4297141947376352, 0.4247464142412669]
GoodReads_MAE_HARS =  [0.32508660558184677, 0.32445000792669704, 0.32916187591465074, 0.332557379275999, 0.3374146421315535, 0.34404708311964205, 0.3409725140367548, 0.34532015553873235, 0.34861563984987226, 0.3552309963754425, 0.3495219951694368]


####### RMSE  #############

fig = plt.figure(1,figsize=(6, 6))

ax1 = plt.subplot(211)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax1.plot(DataClippingScale,Douban_RMSE_HARS,color = 'red',label = 'Douban')
plt.gca().spines["top"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.3)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["left"].set_alpha(0.3)
plt.xticks(fontsize=15,rotation = 270)
plt.yticks(fontsize=15)
plt.xticks(np.arange(0,0.55,0.05))
plt.ylim((0.9,1.0))
plt.ylabel("RMSE",fontsize = 25)
plt.legend(loc='upper left',fontsize = 15)
plt.grid(axis='both', alpha=0.3)



ax2 = plt.subplot(212)
plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax2.plot(DataClippingScale,GoodReads_RMSE_HARS,color = 'limegreen',label = 'GoodReads')
plt.gca().spines["top"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.3)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["left"].set_alpha(0.3)
plt.xticks(fontsize=15,rotation = 270)
plt.yticks(fontsize=15)
plt.xticks(np.arange(0,0.55,0.05))
plt.ylim((0.36,0.46))
plt.xlabel("Data Clipping Scale",fontsize = 25)
plt.ylabel("RMSE",fontsize = 25)
plt.legend(loc='upper left',fontsize = 15)
plt.grid(axis='both', alpha=0.3)


plt.savefig('C:/Users/chopin/Desktop/'+'SW_RMSE.pdf', bbox_inches='tight')

plt.show()









####### MAE  #############

fig = plt.figure(1,figsize=(6, 6))

ax1 = plt.subplot(211)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax1.plot(DataClippingScale,Douban_MAE_HARS,color = 'red',label = 'Douban')
plt.gca().spines["top"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.3)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["left"].set_alpha(0.3)
plt.xticks(fontsize=15,rotation = 270)
plt.yticks(fontsize=15)
plt.xticks(np.arange(0,0.55,0.05))
plt.ylim((0.7,0.8))
plt.ylabel("MAE",fontsize = 25)
plt.legend(loc='upper left',fontsize = 15)
plt.grid(axis='both', alpha=0.3)


ax2 = plt.subplot(212)
plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax2.plot(DataClippingScale,GoodReads_MAE_HARS,color = 'limegreen',label = 'GoodReads')
plt.gca().spines["top"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.3)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["left"].set_alpha(0.3)
plt.xticks(fontsize=15,rotation = 270)
plt.yticks(fontsize=15)
plt.xticks(np.arange(0,0.55,0.05))
plt.ylim((0.3,0.4))
plt.xlabel("Data Clipping Scale",fontsize = 25)
plt.ylabel("MAE",fontsize = 25)
plt.legend(loc='upper left',fontsize = 15)
plt.grid(axis='both', alpha=0.3)


plt.savefig('C:/Users/chopin/Desktop/'+'SW_MAE.pdf', bbox_inches='tight')

plt.show()


