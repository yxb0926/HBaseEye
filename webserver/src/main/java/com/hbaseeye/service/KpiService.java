package com.hbaseeye.service;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
public interface KpiService {
    public List getKpi(String tag, String serverName, Long startTime, Long endTime);
}
