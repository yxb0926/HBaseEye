package com.hbaseeye.service.Impl;

import com.hbaseeye.model.RegionInfo;
import com.hbaseeye.service.HRegionServerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Service
public class HRegionServerServiceImpl implements HRegionServerService {
    @Autowired
    private MongoTemplate mongoTemplate;

    public List getRegionInfo() {
        List <RegionInfo> regionInfoList = null;
        regionInfoList = mongoTemplate.findAll(RegionInfo.class);

        return regionInfoList;
    }
}
