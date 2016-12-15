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


        tagRegionMap.put("ThreadsWaiting", new TableFiledsMap("reginJvmMetrics", "ThreadsWaiting"));
        tagRegionMap.put("ThreadsTerminated", new TableFiledsMap("reginJvmMetrics", "ThreadsTerminated"));
        tagRegionMap.put("MemNonHeapCommittedM", new TableFiledsMap("reginJvmMetrics", "MemNonHeapCommittedM"));
        tagRegionMap.put("GcTimeMillis", new TableFiledsMap("reginJvmMetrics", "GcTimeMillis"));
        tagRegionMap.put("MemHeapMaxM", new TableFiledsMap("reginJvmMetrics", "MemHeapMaxM"));
        tagRegionMap.put("MemHeapUsedM", new TableFiledsMap("reginJvmMetrics", "MemHeapUsedM"));
        tagRegionMap.put("ThreadsBlocked", new TableFiledsMap("reginJvmMetrics", "ThreadsBlocked"));
        tagRegionMap.put("GcTimeMillisConcurrentMarkSweep", new TableFiledsMap("reginJvmMetrics", "GcTimeMillisConcurrentMarkSweep"));
        tagRegionMap.put("GcTimeMillisParNew", new TableFiledsMap("reginJvmMetrics", "GcTimeMillisParNew"));
        tagRegionMap.put("MemHeapCommittedM", new TableFiledsMap("reginJvmMetrics", "MemHeapCommittedM"));
        tagRegionMap.put("GcCountParNew", new TableFiledsMap("reginJvmMetrics", "GcCountParNew"));
        tagRegionMap.put("MemNonHeapMaxM", new TableFiledsMap("reginJvmMetrics", "MemNonHeapMaxM"));
        tagRegionMap.put("GcCountConcurrentMarkSweep", new TableFiledsMap("reginJvmMetrics", "GcCountConcurrentMarkSweep"));
        tagRegionMap.put("ThreadsNew", new TableFiledsMap("reginJvmMetrics", "ThreadsNew"));
        tagRegionMap.put("ThreadsRunnable", new TableFiledsMap("reginJvmMetrics", "ThreadsRunnable"));
        tagRegionMap.put("GcCount", new TableFiledsMap("reginJvmMetrics", "GcCount"));
        tagRegionMap.put("ThreadsTimedWaiting", new TableFiledsMap("reginJvmMetrics", "ThreadsTimedWaiting"));
        tagRegionMap.put("MemMaxM", new TableFiledsMap("reginJvmMetrics", "MemMaxM"));
        tagRegionMap.put("MemNonHeapUsedM", new TableFiledsMap("reginJvmMetrics", "MemNonHeapUsedM"));

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


