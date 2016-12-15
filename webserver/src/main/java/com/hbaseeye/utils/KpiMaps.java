package com.hbaseeye.utils;

import com.hbaseeye.model.TableFiledsMap;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
public class KpiMaps {
    public KpiMaps(){}

    public static Map tagRegionMap = new HashMap();
    public static Map tagMasterMap = new HashMap();
    public static Map typeTableMap = new HashMap();

    static {
        tagRegionMap.put("qps", new TableFiledsMap("regionRequest", "qps"));
        tagRegionMap.put("writeRequestCount", new TableFiledsMap("regionRequest", "writeRequestCount"));
        tagRegionMap.put("readRequestCount",  new TableFiledsMap("regionRequest", "readRequestCount"));
        tagRegionMap.put("totalRequestCount", new TableFiledsMap("regionRequest", "totalRequestCount"));
        tagRegionMap.put("read",  new TableFiledsMap("regionRequest", "read"));
        tagRegionMap.put("write", new TableFiledsMap("regionRequest", "write"));

        tagRegionMap.put("regionCount",  new TableFiledsMap("regionrsfmInfo", "regionCount"));
        tagRegionMap.put("hlogFileSize", new TableFiledsMap("regionrsfmInfo", "hlogFileSize"));
        tagRegionMap.put("storeFileCount", new TableFiledsMap("regionrsfmInfo", "storeFileCount"));
        tagRegionMap.put("hlogFileCount", new TableFiledsMap("regionrsfmInfo", "hlogFileCount"));
        tagRegionMap.put("storeCount", new TableFiledsMap("regionrsfmInfo", "storeCount"));
        tagRegionMap.put("memStoreSize", new TableFiledsMap("regionrsfmInfo", "memStoreSize"));
        tagRegionMap.put("storeFileSize", new TableFiledsMap("regionrsfmInfo", "storeFileSize"));

    }

    static {
        tagMasterMap.put("GcTimeMillisConcurrentMarkSweep", new TableFiledsMap("masterJvmMetrics", "GcTimeMillisConcurrentMarkSweep") );
        tagMasterMap.put("GcTimeMillisParNew", new TableFiledsMap("masterJvmMetrics", "GcTimeMillisParNew") );
        tagMasterMap.put("ThreadsBlocked", new TableFiledsMap("masterJvmMetrics", "ThreadsBlocked") );
        tagMasterMap.put("GcCountParNew", new TableFiledsMap("masterJvmMetrics", "GcCountParNew") );
    }

    static {
        typeTableMap.put("hregion", tagRegionMap);
        typeTableMap.put("hmaster", tagMasterMap);
    }

}


