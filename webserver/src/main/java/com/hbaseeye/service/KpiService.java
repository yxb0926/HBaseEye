package com.hbaseeye.service;

import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Service
public interface KpiService {
    public List getKpi(String type, String tag, String serverName, String startTime, String endTime);
}
