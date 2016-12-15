package com.hbaseeye.service.Impl;

import com.hbaseeye.model.RegionInfo;
import com.hbaseeye.service.HRegionServerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
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
        Query query = new Query();
        query.with(new Sort(Sort.Direction.ASC, "hostname"));


        regionInfoList = mongoTemplate.find(query, RegionInfo.class);

        return regionInfoList;
    }
}
