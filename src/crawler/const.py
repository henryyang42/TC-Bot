# coding: utf-8
ntu_course_dpt_search_url = 'http://nol2.aca.ntu.edu.tw/nol/coursesearch/search_for_02_dpt.php'
base_url = 'http://nol2.aca.ntu.edu.tw/nol/coursesearch/'

all_dept = {
    "1000": "1000 文學院",
    "1010": "1010 中國文學系",
    "1011": "1011 中國文學系國際學生學士班",
    "1020": "1020 外國語文學系",
    "1030": "1030 歷史學系",
    "1040": "1040 哲學系",
    "1050": "1050 人類學系",
    "1060": "1060 圖書資訊學系",
    "1070": "1070 日本語文學系",
    "1080": "1080 應用英語學系",
    "1090": "1090 戲劇學系",
    "1210": "1210 中國文學研究所",
    "1220": "1220 外國語文學研究所",
    "1230": "1230 歷史學研究所",
    "1240": "1240 哲學研究所",
    "1250": "1250 人類學研究所",
    "1260": "1260 圖書資訊學研究所",
    "1270": "1270 日本語文學研究所",
    "1290": "1290 戲劇學研究所",
    "1410": "1410 藝術史研究所",
    "1420": "1420 語言學研究所",
    "1440": "1440 音樂學研究所",
    "1450": "1450 臺灣文學研究所",
    "1460": "1460 華語教學碩士學位學程",
    "1470": "1470 翻譯碩士學位學程",
    "2000": "2000 理學院",
    "2010": "2010 數學系",
    "2020": "2020 物理學系",
    "2030": "2030 化學系",
    "2040": "2040 地質科學系",
    "2050": "2050 動物學系",
    "2051": "2051 動物生物組",
    "2052": "2052 漁業生物組",
    "2060": "2060 植物學系",
    "2070": "2070 心理學系",
    "2080": "2080 地理環境資源學系",
    "2090": "2090 大氣科學系",
    "2210": "2210 數學研究所",
    "2220": "2220 物理學研究所",
    "2230": "2230 化學研究所",
    "2231": "2231 化學所化學組",
    "2232": "2232 化學所化學生物學組",
    "2240": "2240 地質科學研究所",
    "2241": "2241 地質組",
    "2242": "2242 應用地質組",
    "2250": "2250 動物學研究所",
    "2260": "2260 植物學研究所",
    "2270": "2270 心理學研究所",
    "2271": "2271 一般心理學組",
    "2272": "2272 臨床心理學組",
    "2280": "2280 地理環境資源學研究所",
    "2290": "2290 大氣科學研究所",
    "2410": "2410 海洋研究所",
    "2411": "2411 海洋物理組",
    "2412": "2412 海洋生物及漁業組",
    "2413": "2413 海洋地質及地球物理",
    "2414": "2414 海洋化學組",
    "2440": "2440 天文物理研究所",
    "2450": "2450 應用物理學研究所",
    "2460": "2460 應用數學科學研究所",
    "2470": "2470 氣候變遷與永續發展國際學位學程",
    "3000": "3000 社會科學院",
    "3020": "3020 政治學系",
    "3021": "3021 政治理論組",
    "3022": "3022 國際關係組",
    "3023": "3023 公共行政組",
    "3030": "3030 經濟學系",
    "3050": "3050 社會學系",
    "3051": "3051 社會學組",
    "3052": "3052 社會工作組",
    "3100": "3100 社會工作學系",
    "3220": "3220 政治學研究所",
    "3230": "3230 經濟學研究所",
    "3250": "3250 社會學研究所",
    "3300": "3300 社會工作學研究所",
    "3410": "3410 國家發展研究所",
    "3420": "3420 新聞研究所",
    "3430": "3430 公共事務研究所",
    "4000": "4000 醫學院",
    "4010": "4010 醫學系",
    "4020": "4020 牙醫學系",
    "4030": "4030 藥學系",
    "4031": "4031 藥學系六年制",
    "4040": "4040 醫學檢驗暨生物技術學系(原醫事技術學系)",
    "4060": "4060 護理學系",
    "4080": "4080 物理治療學系",
    "4090": "4090 職能治療學系",
    "4200": "4200 醫學院暨公共衛生學院共同課程",
    "4210": "4210 臨床醫學研究所",
    "4220": "4220 臨床牙醫學研究所",
    "4230": "4230 藥學研究所",
    "4231": "4231 藥學系博士班藥物科技組",
    "4232": "4232 藥學系博士班分子醫藥組",
    "4240": "4240 醫事技術學研究所",
    "4260": "4260 護理學研究所",
    "4280": "4280 物理治療學研究所",
    "4290": "4290 職能治療學研究所",
    "4410": "4410 生理學研究所",
    "4420": "4420 生化學研究所",
    "4430": "4430 藥理學研究所",
    "4440": "4440 病理學研究所",
    "4450": "4450 微生物學研究所",
    "4451": "4451 微生物及免疫學組",
    "4452": "4452 寄生蟲組",
    "4460": "4460 解剖學暨細胞生物學研究所",
    "4470": "4470 毒理學研究所",
    "4480": "4480 分子醫學研究所",
    "4490": "4490 免疫學研究所",
    "4500": "4500 口腔生物科學研究所",
    "4510": "4510 臨床藥學研究所",
    "4520": "4520 法醫學研究所",
    "4530": "4530 腫瘤醫學研究所",
    "4540": "4540 腦與心智科學研究所",
    "4550": "4550 基因體暨蛋白體醫學研究所",
    "4560": "4560 轉譯醫學博士學位學程",
    "4570": "4570 醫學教育暨生醫倫理研究所",
    "4580": "4580 醫療器材與醫學影像研究所",
    "5000": "5000 工學院",
    "5010": "5010 土木工程學系",
    "5020": "5020 機械工程學系",
    "5040": "5040 化學工程學系",
    "5050": "5050 工程科學及海洋工程學系",
    "5070": "5070 材料科學與工程學系",
    "5210": "5210 土木工程學研究所",
    "5211": "5211 大地工程組",
    "5212": "5212 結構工程組",
    "5213": "5213 水利工程組",
    "5215": "5215 交通工程組",
    "5216": "5216 電腦輔助工程組",
    "5217": "5217 營建工程與管理組",
    "5220": "5220 機械工程學研究所",
    "5221": "5221 流體力學組",
    "5223": "5223 熱學組",
    "5224": "5224 航空工程組",
    "5225": "5225 固體力學組",
    "5226": "5226 設計組",
    "5227": "5227 製造組",
    "5228": "5228 系統控制組",
    "5240": "5240 化學工程學研究所",
    "5250": "5250 工程科學及海洋工程學研究所",
    "5270": "5270 材料科學與工程學研究所",
    "5410": "5410 環境工程學研究所",
    "5430": "5430 應用力學研究所",
    "5440": "5440 建築與城鄉研究所",
    "5460": "5460 工業工程學研究所",
    "5480": "5480 醫學工程學研究所",
    "5490": "5490 高分子科學與工程學研究所",
    "5500": "5500 綠色永續材料與精密元件博士學位學程",
    "6000": "6000 生物資源暨農學院",
    "6010": "6010 農藝學系",
    "6020": "6020 生物環境系統工程學系",
    "6030": "6030 農業化學系",
    "6031": "6031 土壤肥料組",
    "6032": "6032 農產製造組",
    "6040": "6040 植物病蟲害學系",
    "6050": "6050 森林環境暨資源學系",
    "6051": "6051 育林組",
    "6052": "6052 資源管理組",
    "6053": "6053 森林工業組",
    "6054": "6054 森林資源保育組",
    "6060": "6060 動物科學技術學系",
    "6070": "6070 農業經濟學系",
    "6080": "6080 園藝暨景觀學系",
    "6090": "6090 獸醫學系",
    "6100": "6100 生物產業傳播暨發展學系",
    "6101": "6101 推廣教育組",
    "6102": "6102 鄉村社會組",
    "6110": "6110 生物產業機電工程學系",
    "6120": "6120 昆蟲學系",
    "6130": "6130 植物病理與微生物學系",
    "6210": "6210 農藝學研究所",
    "6211": "6211 作物科學組",
    "6212": "6212 生物統計學組",
    "6220": "6220 生物環境系統工程學研究所",
    "6230": "6230 農業化學研究所",
    "6234": "6234 土壤環境與植物營養組",
    "6235": "6235 生物工業化學組",
    "6236": "6236 生物化學組",
    "6237": "6237 營養科學組",
    "6238": "6238 微生物學組",
    "6250": "6250 森林環境暨資源學研究所",
    "6260": "6260 動物科學技術學研究所",
    "6270": "6270 農業經濟學研究所",
    "6280": "6280 園藝學研究所",
    "6281": "6281 園藝作物組",
    "6282": "6282 園產品處理及加工組",
    "6283": "6283 造園組",
    "6290": "6290 獸醫學研究所",
    "6300": "6300 生物產業傳播暨發展學研究所",
    "6310": "6310 生物產業機電工程學所",
    "6320": "6320 昆蟲學研究所",
    "6330": "6330 植物病理與微生物學研究所",
    "6410": "6410 食品科技研究所",
    "6420": "6420 生物科技研究所",
    "6430": "6430 臨床動物醫學研究所",
    "6440": "6440 分子暨比較病理生物學研究所",
    "6450": "6450 植物醫學碩士學位學程",
    "7000": "7000 管理學院",
    "7010": "7010 工商管理學系",
    "7011": "7011 企業管理組",
    "7012": "7012 科技管理組",
    "7013": "7013 工商管理系企業管理組英文專班",
    "7020": "7020 會計學系",
    "7030": "7030 財務金融學系",
    "7040": "7040 國際企業學系",
    "7050": "7050 資訊管理學系",
    "7060": "7060 企業管理學系",
    "7220": "7220 會計學研究所",
    "7230": "7230 財務金融學研究所",
    "7240": "7240 國際企業學研究所",
    "7250": "7250 資訊管理學研究所",
    "7400": "7400 高階管理碩士專班(EMBA)",
    "7410": "7410 商學研究所",
    "7420": "7420 知識管理組",
    "7430": "7430 管理學院高階公共管理組",
    "7440": "7440 管理學院會計與管理決策組",
    "7450": "7450 管理學院財務金融組",
    "7460": "7460 管理學院國際企業管理組",
    "7470": "7470 管理學院資訊管理組",
    "7480": "7480 管理學院商學組",
    "7490": "7490 管理學院企業管理碩士專班",
    "7500": "7500 臺大-復旦EMBA",
    "7510": "7510 創業創新管理碩士在職專班",
    "8000": "8000 公共衛生學院",
    "8010": "8010 公共衛生學系",
    "8410": "8410 職業醫學與工業衛生研究所",
    "8420": "8420 流行病學研究所",
    "8430": "8430 醫療機構管理研究所",
    "8440": "8440 環境衛生研究所",
    "8470": "8470 公共衛生碩士學位學程",
    "8480": "8480 健康政策與管理研究所",
    "8481": "8481 健康促進組",
    "8482": "8482 健康服務與產業組",
    "8490": "8490 流行病學與預防醫學研究所",
    "8491": "8491 流預所流行病學組",
    "8492": "8492 流預所生物醫學統計組",
    "8493": "8493 流預所預防醫學組",
    "8500": "8500 健康行為與社區科學研究所",
    "9000": "9000 電機資訊學院",
    "9010": "9010 電機工程學系",
    "9020": "9020 資訊工程學系",
    "9210": "9210 電機工程學研究所",
    "9220": "9220 資訊工程學研究所",
    "9410": "9410 光電工程學研究所",
    "9420": "9420 電信工程學研究所",
    "9430": "9430 電子工程學研究所",
    "9440": "9440 資訊網路與多媒體研究所",
    "9450": "9450 生醫電子與資訊學研究所",
    "0020": "0020 體育室",
    "0030": "0030 軍訓室",
    "0040": "0040 外語教學暨資源中心",
    "0050": "0050 學務處課外活動組",
    "A000": "A000 法律學院",
    "A010": "A010 法律學系",
    "A011": "A011 法學組",
    "A012": "A012 司法組",
    "A013": "A013 財法組",
    "A210": "A210 法律研究所",
    "A408": "A408 教學發展中心",
    "A410": "A410 科際整合法律學研究所",
    "B000": "B000 生命科學院",
    "B010": "B010 生命科學系",
    "B020": "B020 生化科技學系",
    "B210": "B210 生命科學所",
    "B220": "B220 生化科技研究所",
    "B420": "B420 植物科學研究所",
    "B430": "B430 分子與細胞生物學研究所",
    "B440": "B440 生態學與演化生物學研究所",
    "B450": "B450 漁業科學研究所",
    "B460": "B460 生化科學研究所",
    "B470": "B470 微生物與生化學研究所",
    "B471": "B471 生物工業組",
    "B472": "B472 生物化學組",
    "B473": "B473 營養科學組",
    "B474": "B474 微生物學組",
    "B480": "B480 基因體與系統生物學學位學程",
    "G010": "G010 台北教育大學",
    "H000": "H000 共同教育中心",
    "H010": "H010 通識教育組",
    "H020": "H020 共同教育組",
    "H410": "H410 統計碩士學位學程",
    "H420": "H420 運動設施與健康管理碩士學位學程",
    "J000": "J000 產業研發專班",
    "J100": "J100 電機產業專班",
    "J110": "J110 資訊產業專班",
    "K000": "K000 三校聯盟",
    "K010": "K010 國立臺灣師範大學",
    "K020": "K020 國立臺灣科技大學",
    "K030": "K030 國立臺北教育大學",
    "Q010": "Q010 寫作教學中心",
    "Q020": "Q020 生命教育研發育成中心",
    "Z010": "Z010 創新設計學院"
}
