__author__ = 'Leo'
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import matplotlib.pyplot as plt
import math

dictforplot = {'120': {'side': 0.0, 'down': 0.0, 'far': 0.027777777777777776, 'center': 0.0, 'aside': 0.0, 'up': 0.0, 'right': 0.2951388888888889, 'left': 0.2517361111111111, 'near_gen': 0.1684027777777778, 'hindpart': 0.0, 'front': 0.015625, 'behind_gen': 0.09895833333333333, 'edge': 0.2222222222222222, 'frontpart': 0.0}, '300': {'side': 0.011482812822098537, 'down': 0.0289856968428397, 'far': 0.004535147392290249, 'center': 0.017647828362114076, 'aside': 0.006366649223792081, 'up': 0.011904761904761904, 'right': 0.5359507555936127, 'left': 0.023164087896230753, 'near_gen': 0.14267047436690292, 'hindpart': 0.0, 'front': 0.11523080094508667, 'behind_gen': 0.0833829365079365, 'edge': 0.09825947861662147, 'frontpart': 0.0}, '75': {'side': 0.007936507936507936, 'down': 0.0, 'far': 0.012265512265512264, 'center': 0.027705627705627706, 'aside': 0.010714285714285714, 'up': 0.0, 'right': 0.023356009070294784, 'left': 0.5830550401978972, 'near_gen': 0.10957019171304885, 'hindpart': 0.0, 'front': 0.05551948051948052, 'behind_gen': 0.10034013605442177, 'edge': 0.06456916099773242, 'frontpart': 0.0}, '315': {'side': 0.0, 'down': 0.0496031746031746, 'far': 0.016534391534391533, 'center': 0.06580687830687831, 'aside': 0.0, 'up': 0.0, 'right': 0.2781084656084656, 'left': 0.12962962962962962, 'near_gen': 0.14682539682539683, 'hindpart': 0.0, 'front': 0.21164021164021166, 'behind_gen': 0.14351851851851852, 'edge': 0.03869047619047619, 'frontpart': 0.009259259259259259}, '105': {'side': 0.006604506604506604, 'down': 0.003205128205128205, 'far': 0.011538461538461539, 'center': 0.013635723251107866, 'aside': 0.0019723865877712033, 'up': 0.014731849347233962, 'right': 0.051506186121570735, 'left': 0.5615621557929251, 'near_gen': 0.045371295371295375, 'hindpart': 0.0, 'front': 0.013014763014763014, 'behind_gen': 0.2005088928165851, 'edge': 0.1531492012261243, 'frontpart': 0.0}, '30': {'side': 0.013187429854096521, 'down': 0.01335978835978836, 'far': 0.014257655924322592, 'center': 0.029910213243546577, 'aside': 0.002777777777777778, 'up': 0.010101010101010102, 'right': 0.08134118967452302, 'left': 0.2118606701940035, 'near_gen': 0.09813612313612316, 'hindpart': 0.0, 'front': 0.29302148468815137, 'behind_gen': 0.09840067340067339, 'edge': 0.25437309603976266, 'frontpart': 0.0031746031746031746}, '255': {'side': 0.004329004329004329, 'down': 0.012987012987012988, 'far': 0.01507936507936508, 'center': 0.02694805194805195, 'aside': 0.011868686868686869, 'up': 0.0, 'right': 0.3600649350649351, 'left': 0.10692640692640694, 'near_gen': 0.10097402597402597, 'hindpart': 0.0, 'front': 0.23712121212121215, 'behind_gen': 0.0332972582972583, 'edge': 0.15764790764790765, 'frontpart': 0.004329004329004329}, '285': {'side': 0.0, 'down': 0.009680134680134681, 'far': 0.008796296296296295, 'center': 0.009217171717171718, 'aside': 0.012962962962962963, 'up': 0.0, 'right': 0.49796176046176044, 'left': 0.06717171717171717, 'near_gen': 0.15521885521885523, 'hindpart': 0.0, 'front': 0.048544973544973544, 'behind_gen': 0.02680976430976431, 'edge': 0.23808922558922563, 'frontpart': 0.005050505050505051}, '345': {'side': 0.005050505050505051, 'down': 0.047053872053872056, 'far': 0.011994949494949496, 'center': 0.005050505050505051, 'aside': 0.0, 'up': 0.0, 'right': 0.09255050505050505, 'left': 0.01111111111111111, 'near_gen': 0.12260101010101009, 'hindpart': 0.0, 'front': 0.5322390572390572, 'behind_gen': 0.015151515151515152, 'edge': 0.1862373737373737, 'frontpart': 0.01893939393939394}, '330': {'side': 0.02354978354978355, 'down': 0.025324675324675323, 'far': 0.005714285714285714, 'center': 0.018917748917748917, 'aside': 0.0, 'up': 0.011428571428571429, 'right': 0.1777056277056277, 'left': 0.03428571428571429, 'near_gen': 0.09878787878787879, 'hindpart': 0.0, 'front': 0.48764069264069265, 'behind_gen': 0.09976190476190476, 'edge': 0.0845021645021645, 'frontpart': 0.0}, '270': {'side': 0.012777777777777777, 'down': 0.011904761904761904, 'far': 0.01414141414141414, 'center': 0.03885281385281385, 'aside': 0.0027777777777777775, 'up': 0.0, 'right': 0.5040909090909091, 'left': 0.059642857142857136, 'near_gen': 0.09570707070707073, 'hindpart': 0.0, 'front': 0.11833333333333335, 'behind_gen': 0.09261904761904763, 'edge': 0.09682539682539683, 'frontpart': 0.0}, '45': {'side': 0.010141093474426807, 'down': 0.038580246913580245, 'far': 0.009259259259259259, 'center': 0.03990299823633157, 'aside': 0.006172839506172839, 'up': 0.009259259259259259, 'right': 0.15379990379990377, 'left': 0.34766313932980597, 'near_gen': 0.15506253006253004, 'hindpart': 0.0, 'front': 0.22829485329485327, 'behind_gen': 0.0308641975308642, 'edge': 0.07716049382716049, 'frontpart': 0.009259259259259259}, '165': {'side': 0.025859788359788357, 'down': 0.0, 'far': 0.01574074074074074, 'center': 0.0, 'aside': 0.0, 'up': 0.04010942760942761, 'right': 0.0, 'left': 0.11675685425685425, 'near_gen': 0.05040283790283791, 'hindpart': 0.0, 'front': 0.011706349206349206, 'behind_gen': 0.6686026936026935, 'edge': 0.07857744107744108, 'frontpart': 0.0}, '15': {'side': 0.0, 'down': 0.03857142857142857, 'far': 0.0, 'center': 0.025714285714285714, 'aside': 0.007142857142857143, 'up': 0.0, 'right': 0.09142857142857143, 'left': 0.16071428571428573, 'near_gen': 0.18071428571428572, 'hindpart': 0.0, 'front': 0.562142857142857, 'behind_gen': 0.05642857142857143, 'edge': 0.027142857142857142, 'frontpart': 0.0}, '195': {'side': 0.003968253968253968, 'down': 0.03571428571428571, 'far': 0.015873015873015872, 'center': 0.007936507936507936, 'aside': 0.0, 'up': 0.0, 'right': 0.2599206349206349, 'left': 0.09325396825396826, 'near_gen': 0.09722222222222221, 'hindpart': 0.003968253968253968, 'front': 0.11706349206349206, 'behind_gen': 0.15818903318903318, 'edge': 0.09325396825396826, 'frontpart': 0.0}, '135': {'side': 0.003968253968253968, 'down': 0.0, 'far': 0.02056277056277056, 'center': 0.013888888888888888, 'aside': 0.003968253968253968, 'up': 0.03251162417829084, 'right': 0.11415343915343915, 'left': 0.20342712842712843, 'near_gen': 0.14128587461920797, 'hindpart': 0.0, 'front': 0.02119608786275453, 'behind_gen': 0.3994668911335578, 'edge': 0.17030222863556194, 'frontpart': 0.0}, '150': {'side': 0.01717171717171717, 'down': 0.017142857142857144, 'far': 0.03811188811188811, 'center': 0.01748917748917749, 'aside': 0.0, 'up': 0.023737373737373738, 'right': 0.06136752136752136, 'left': 0.18858141858141858, 'near_gen': 0.13264402264402264, 'hindpart': 0.0, 'front': 0.07428571428571429, 'behind_gen': 0.3235076035076035, 'edge': 0.17813741813741812, 'frontpart': 0.0}, '210': {'side': 0.012739641311069881, 'down': 0.017316017316017316, 'far': 0.011982065553494126, 'center': 0.027705627705627706, 'aside': 0.0035714285714285718, 'up': 0.005952380952380952, 'right': 0.23112244897959183, 'left': 0.08968769325912183, 'near_gen': 0.14921150278293138, 'hindpart': 0.004081632653061224, 'front': 0.09823747680890538, 'behind_gen': 0.2902906617192331, 'edge': 0.1608379715522573, 'frontpart': 0.004329004329004329}, '240': {'side': 0.004629629629629629, 'down': 0.009680134680134681, 'far': 0.0, 'center': 0.009680134680134681, 'aside': 0.0, 'up': 0.018849206349206348, 'right': 0.2767857142857143, 'left': 0.040740740740740744, 'near_gen': 0.18906325156325154, 'hindpart': 0.0, 'front': 0.17997234247234248, 'behind_gen': 0.1488997113997114, 'edge': 0.11044973544973546, 'frontpart': 0.0047619047619047615}, '0': {'side': 0.006060606060606061, 'down': 0.03383838383838384, 'far': 0.005, 'center': 0.039242424242424245, 'aside': 0.0, 'up': 0.005, 'right': 0.2510606060606061, 'left': 0.08242424242424243, 'near_gen': 0.051010101010101006, 'hindpart': 0.0, 'front': 0.40863636363636363, 'behind_gen': 0.02333333333333333, 'edge': 0.09151515151515151, 'frontpart': 0.006060606060606061}, '180': {'side': 0.0, 'down': 0.027777777777777776, 'far': 0.0, 'center': 0.008333333333333333, 'aside': 0.009259259259259259, 'up': 0.01759259259259259, 'right': 0.1851851851851852, 'left': 0.009259259259259259, 'near_gen': 0.018518518518518517, 'hindpart': 0.0, 'front': 0.06481481481481481, 'behind_gen': 0.4961640211640212, 'edge': 0.045370370370370366, 'frontpart': 0.0}, '225': {'side': 0.010416666666666666, 'down': 0.0, 'far': 0.014705882352941176, 'center': 0.00625, 'aside': 0.00625, 'up': 0.010416666666666666, 'right': 0.14829545454545456, 'left': 0.3148061497326203, 'near_gen': 0.2624331550802139, 'hindpart': 0.014928698752228164, 'front': 0.0125, 'behind_gen': 0.3408088235294118, 'edge': 0.06706773618538325, 'frontpart': 0.0}, '90': {'side': 0.014991181657848324, 'down': 0.0, 'far': 0.010493827160493827, 'center': 0.012566137566137565, 'aside': 0.005864197530864198, 'up': 0.008333333333333333, 'right': 0.16408529741863073, 'left': 0.44501763668430333, 'near_gen': 0.13784672118005453, 'hindpart': 0.0033670033670033673, 'front': 0.06355218855218855, 'behind_gen': 0.070679012345679, 'edge': 0.20234888568221904, 'frontpart': 0.0}, '60': {'side': 0.0248015873015873, 'down': 0.026785714285714284, 'far': 0.00625, 'center': 0.026785714285714284, 'aside': 0.015178571428571428, 'up': 0.0, 'right': 0.02212301587301587, 'left': 0.5167658730158731, 'near_gen': 0.0248015873015873, 'hindpart': 0.0, 'front': 0.07668650793650794, 'behind_gen': 0.019444444444444445, 'edge': 0.3825396825396825, 'frontpart': 0.0}}

dictforplot0 = {'270': {'aside': 0.0035714285714285713, 'center': 0.03387849897930543, 'right': 0.5034768766018767, 'frontpart': 0.0, 'edge': 0.09703092515592515, 'behind_gen': 0.09510160284353833, 'left': 0.05890852390852391, 'front': 0.12091811414392059, 'far': 0.013125000000000001, 'down': 0.013846153846153847, 'hindpart': 0.0, 'near_gen': 0.1018155586905587, 'up': 0.0, 'side': 0.01019696029776675}, '30': {'aside': 0.003003003003003003, 'center': 0.031206603428825648, 'right': 0.07849168613057501, 'frontpart': 0.004115226337448559, 'edge': 0.2771806528750973, 'behind_gen': 0.10653987320653988, 'left': 0.1949883415161193, 'front': 0.28564516897850234, 'far': 0.013786008230452673, 'down': 0.011561561561561563, 'hindpart': 0.0, 'near_gen': 0.09401266345710789, 'up': 0.004115226337448559, 'side': 0.008083480305702526}, '315': {'aside': 0.0, 'center': 0.07283653846153847, 'right': 0.2533653846153846, 'frontpart': 0.010416666666666666, 'edge': 0.036778846153846155, 'behind_gen': 0.13854166666666667, 'left': 0.13020833333333334, 'front': 0.19863782051282053, 'far': 0.018028846153846156, 'down': 0.054086538461538464, 'hindpart': 0.0, 'near_gen': 0.14567307692307693, 'up': 0.0, 'side': 0.0}, '165': {'aside': 0.0, 'center': 0.0, 'right': 0.0, 'frontpart': 0.0, 'edge': 0.07794252585919252, 'behind_gen': 0.693025718025718, 'left': 0.11419857357357356, 'front': 0.014506172839506172, 'far': 0.01804617117117117, 'down': 0.0, 'hindpart': 0.0, 'near_gen': 0.04961419753086419, 'up': 0.04106919419419419, 'side': 0.032060185185185185}, '120': {'aside': 0.0, 'center': 0.0, 'right': 0.2771164021164021, 'frontpart': 0.0, 'edge': 0.25, 'behind_gen': 0.1078042328042328, 'left': 0.23214285714285715, 'front': 0.018518518518518517, 'far': 0.03571428571428571, 'down': 0.0, 'hindpart': 0.0, 'near_gen': 0.1845238095238095, 'up': 0.0, 'side': 0.0}, '150': {'aside': 0.0, 'center': 0.02031063321385902, 'right': 0.05051203277009729, 'frontpart': 0.0, 'edge': 0.18628605564089434, 'behind_gen': 0.34904420549581844, 'left': 0.1879330943847073, 'front': 0.07096774193548387, 'far': 0.03835978835978836, 'down': 0.01935483870967742, 'hindpart': 0.0, 'near_gen': 0.138931558286397, 'up': 0.021957671957671957, 'side': 0.014285714285714285}, '45': {'aside': 0.007936507936507936, 'center': 0.035950854700854705, 'right': 0.15524352191018856, 'frontpart': 0.011408730158730158, 'edge': 0.07807539682539683, 'behind_gen': 0.022222222222222223, 'left': 0.3418879731379731, 'front': 0.22945552389996832, 'far': 0.003968253968253968, 'down': 0.035470085470085476, 'hindpart': 0.0, 'near_gen': 0.16110376249265138, 'up': 0.011111111111111112, 'side': 0.003472222222222222}, '240': {'aside': 0.0, 'center': 0.011381172839506171, 'right': 0.27639185660018994, 'frontpart': 0.006172839506172839, 'edge': 0.11618589743589744, 'behind_gen': 0.1282765939015939, 'left': 0.0429749460999461, 'front': 0.192554012345679, 'far': 0.0, 'down': 0.011381172839506171, 'hindpart': 0.0, 'near_gen': 0.2031665479582146, 'up': 0.021153846153846155, 'side': 0.005208333333333333}, '135': {'aside': 0.004273504273504274, 'center': 0.007276507276507277, 'right': 0.11785375118708451, 'frontpart': 0.0, 'edge': 0.18119727633616522, 'behind_gen': 0.40818047137491575, 'left': 0.1920651802596247, 'front': 0.024534737729182174, 'far': 0.014531893004115226, 'down': 0.0, 'hindpart': 0.0, 'near_gen': 0.12990847990847992, 'up': 0.03212780087780088, 'side': 0.0}, '345': {'aside': 0.0, 'center': 0.0, 'right': 0.08341704800038133, 'frontpart': 0.012125220458553791, 'edge': 0.19065255731922398, 'behind_gen': 0.012345679012345678, 'left': 0.012837837837837839, 'front': 0.5545509795509795, 'far': 0.008333333333333333, 'down': 0.043229688021354684, 'hindpart': 0.0, 'near_gen': 0.1203626245292912, 'up': 0.0, 'side': 0.0}, '225': {'aside': 0.006756756756756757, 'center': 0.006756756756756757, 'right': 0.13453453453453454, 'frontpart': 0.0, 'edge': 0.07585470085470086, 'behind_gen': 0.32182085932085924, 'left': 0.31180603680603686, 'front': 0.013513513513513514, 'far': 0.009615384615384616, 'down': 0.0, 'hindpart': 0.018874643874643875, 'near_gen': 0.2796662046662047, 'up': 0.0125, 'side': 0.0125}, '195': {'aside': 0.0, 'center': 0.008928571428571428, 'right': 0.24910714285714286, 'frontpart': 0.0, 'edge': 0.09336734693877552, 'behind_gen': 0.1577620791906506, 'left': 0.09834183673469388, 'front': 0.09910714285714287, 'far': 0.00510204081632653, 'down': 0.04196428571428572, 'hindpart': 0.00510204081632653, 'near_gen': 0.11339285714285716, 'up': 0.0, 'side': 0.004464285714285714}, '330': {'aside': 0.0, 'center': 0.021551328002940906, 'right': 0.19475783475783476, 'frontpart': 0.0, 'edge': 0.1027479091995221, 'behind_gen': 0.10127837514934289, 'left': 0.025806451612903226, 'front': 0.4988732653248782, 'far': 0.0064516129032258064, 'down': 0.022507122507122508, 'hindpart': 0.0, 'near_gen': 0.10716110651594522, 'up': 0.012903225806451613, 'side': 0.014814814814814814}, '255': {'aside': 0.008963044677330391, 'center': 0.021338302588302587, 'right': 0.35699538824538823, 'frontpart': 0.005291005291005291, 'edge': 0.16777044902044902, 'behind_gen': 0.03355906927335499, 'left': 0.10765676390676392, 'front': 0.23789733611162187, 'far': 0.012824048538334253, 'down': 0.010582010582010581, 'hindpart': 0.0, 'near_gen': 0.10655361994647708, 'up': 0.0, 'side': 0.0}, '0': {'aside': 0.0, 'center': 0.04584584584584585, 'right': 0.2509209209209209, 'frontpart': 0.007407407407407407, 'edge': 0.09546546546546547, 'behind_gen': 0.020810810810810813, 'left': 0.08325325325325325, 'front': 0.4013638638638639, 'far': 0.005405405405405406, 'down': 0.01875, 'hindpart': 0.0, 'near_gen': 0.04068443443443444, 'up': 0.005405405405405406, 'side': 0.0}, '75': {'aside': 0.011583011583011584, 'center': 0.026405870155870155, 'right': 0.025402806652806652, 'frontpart': 0.0, 'edge': 0.060641096355382076, 'behind_gen': 0.10549450549450548, 'left': 0.5835922264493693, 'front': 0.05657685746971461, 'far': 0.00510204081632653, 'down': 0.0, 'hindpart': 0.0, 'near_gen': 0.10530192673049815, 'up': 0.0, 'side': 0.009566326530612245}, '180': {'aside': 0.010416666666666666, 'center': 0.009009009009009009, 'right': 0.17708333333333334, 'frontpart': 0.0, 'edge': 0.05067567567567567, 'behind_gen': 0.4857934857934858, 'left': 0.010416666666666666, 'front': 0.0625, 'far': 0.0, 'down': 0.03125, 'hindpart': 0.0, 'near_gen': 0.020833333333333332, 'up': 0.019425675675675675, 'side': 0.0}, '60': {'aside': 0.016372141372141373, 'center': 0.028846153846153848, 'right': 0.024184641372141373, 'frontpart': 0.0, 'edge': 0.3840793918918919, 'behind_gen': 0.021326013513513514, 'left': 0.4909043659043659, 'front': 0.06971153846153846, 'far': 0.006756756756756757, 'down': 0.028846153846153848, 'hindpart': 0.0, 'near_gen': 0.027043269230769232, 'up': 0.0, 'side': 0.027043269230769232}, '90': {'aside': 0.006475225225225225, 'center': 0.014102564102564105, 'right': 0.1567164386608831, 'frontpart': 0.0, 'edge': 0.22188967813967816, 'behind_gen': 0.0716403903903904, 'left': 0.4411887849387849, 'front': 0.05555555555555555, 'far': 0.012030780780780782, 'down': 0.0, 'hindpart': 0.004115226337448559, 'near_gen': 0.13847217944440166, 'up': 0.009009009009009009, 'side': 0.01201923076923077}, '300': {'aside': 0.007282400139542997, 'center': 0.020314746654032368, 'right': 0.5423977696299125, 'frontpart': 0.0, 'edge': 0.095124141999142, 'behind_gen': 0.08483866519580804, 'left': 0.019614512471655327, 'front': 0.12032700380914668, 'far': 0.004979395604395604, 'down': 0.026524410006552868, 'hindpart': 0.0, 'near_gen': 0.134880588005588, 'up': 0.006696428571428571, 'side': 0.00804552590266876}, '15': {'aside': 0.007692307692307693, 'center': 0.021621621621621623, 'right': 0.0962962962962963, 'frontpart': 0.0, 'edge': 0.029313929313929316, 'behind_gen': 0.05353815353815354, 'left': 0.15654885654885656, 'front': 0.5625548625548626, 'far': 0.0, 'down': 0.04158004158004158, 'hindpart': 0.0, 'near_gen': 0.16235466235466234, 'up': 0.0, 'side': 0.0}, '105': {'aside': 0.0021367521367521365, 'center': 0.012762762762762761, 'right': 0.049491249491249494, 'frontpart': 0.0, 'edge': 0.1496697881313266, 'behind_gen': 0.20270722963030652, 'left': 0.5658988235911313, 'front': 0.016035816035816036, 'far': 0.014166914166914166, 'down': 0.0038461538461538464, 'hindpart': 0.0, 'near_gen': 0.04513947590870668, 'up': 0.016726320572474418, 'side': 0.002747252747252747}, '285': {'aside': 0.014961389961389961, 'center': 0.010677344010677343, 'right': 0.4834060250726917, 'frontpart': 0.006172839506172839, 'edge': 0.2561609228275895, 'behind_gen': 0.019465894465894466, 'left': 0.06740073406740073, 'front': 0.03631607798274465, 'far': 0.010456885456885456, 'down': 0.006172839506172839, 'hindpart': 0.0, 'near_gen': 0.17189808856475522, 'up': 0.0, 'side': 0.0}, '210': {'aside': 0.003861003861003861, 'center': 0.03258973258973259, 'right': 0.21918346918346918, 'frontpart': 0.005291005291005291, 'edge': 0.17957242957242958, 'behind_gen': 0.29194194194194195, 'left': 0.0825897325897326, 'front': 0.09894179894179896, 'far': 0.014443014443014442, 'down': 0.015873015873015872, 'hindpart': 0.005291005291005291, 'near_gen': 0.164964964964965, 'up': 0.0071428571428571435, 'side': 0.005291005291005291}}
plotx = []
plotpol = []
plotright = []
plotleft = []
plotfront = []
plotrear = []
plotpol2 = []
for i in sorted(dictforplot, key = int):
    plotx.append(int(i))
    plotpol.append((360-int(i))*np.pi/180)
    plotpol2.append((int(i))*np.pi/180)
    plotright.append(dictforplot[i]['right'])
    plotleft.append(dictforplot[i]['left'])
    plotfront.append(dictforplot[i]['front'])

plt.polar(plotpol, plotfront, color= 'r')
# plt.polar(plotpol2, plotleft)
plt.show()

# plt.axis([0,360, 0, 1])











# thetalist = [-0.08333333333333333, 0.75, -0.3333333333333333, 0.5833333333333334, 0.25, 0.8333333333333334, -0.4166666666666667, 0.6666666666666666,
#              -0.5, 0.4166666666666667, 0.16666666666666666, -0.5833333333333334, -0.9166666666666666, -0.8333333333333334, -0.6666666666666666, -0.75,
#              0.08333333333333333, 0.9166666666666666, -0.16666666666666666, -0.25, 0.5, 1.0, 0.3333333333333333, 0.0]
# tlist = []
# for i in thetalist:
#     if i <0:
#         i = (2 + i)*np.pi
#     else:
#         i = i*np.pi
#     tlist.append(i)

#
# r_list = np.array([0.0, 0.13333333333333333, 0.0, 0.7333333333333333, 0.3548387096774194, 0.5, 0.6666666666666666, 0.0, 0.19444444444444445, 0.0,
#                    0.3611111111111111, 0.0, 0.0, 0.6923076923076923, 0.2, 0.0, 0.0, 0.5151515151515151, 0.0, 0.034482758620689655, 0.0, 0.0, 0.21621621621621623, 0.0])
# rr = []
# for i in r_list:
#     i = 1 - i
#     rr.append(i)
#
# def f(x):
#     for i, j in enumerate(thetalist):
#         return r_list[i]
#
# r = np.arange(0, 3.0, 0.01)
# k = [1, 1]
#
# theta = 2 * np.pi * r
#
# ax = plt.subplot(111, projection='polar')
# # ax.plot(theta, r, color='r', linewidth=3)
# ax.plot(2, 0.75, color='y', linewidth=3, marker = "o")
# # for i in thetalist:
# # ax.plot(tlist, rr, color='r', marker = "o", linestyle = "--")
# plt.polar(tlist, rr, marker ='*', color = 'y', label = "random dots")
#
# ax.set_rmax(1.0)
# ax.grid(True)
#
# ax.set_title("random dots", va='bottom')
# plt.show()
