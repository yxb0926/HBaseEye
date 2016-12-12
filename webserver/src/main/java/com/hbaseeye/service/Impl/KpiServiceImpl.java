package com.hbaseeye.service.Impl;

import com.hbaseeye.model.TableFiledsMap;
import com.hbaseeye.service.KpiService;
import com.hbaseeye.utils.KpiMaps;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Service
public class KpiServiceImpl implements KpiService {
    public List getKpi(String type, String tag, String serverName, Long startTime, Long endTime) {
        KpiMaps kpiMaps = new KpiMaps();
        Map<String, TableFiledsMap> map = (Map<String, TableFiledsMap>) kpiMaps.typeTableMap.get("hregion");
        System.out.println(map);
        System.out.println(map.get("qps").getTableName());
        System.out.println(map.get("qps").getFiledName());
        return null;
    }

}
