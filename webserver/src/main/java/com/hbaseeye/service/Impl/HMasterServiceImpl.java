package com.hbaseeye.service.Impl;

import com.hbaseeye.model.MasterInfo;
import com.hbaseeye.service.HMasterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.mongo.MongoProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Service
@EnableConfigurationProperties(MongoProperties.class)
public class HMasterServiceImpl implements HMasterService {

    @Autowired
    private MongoTemplate mongoTemplate;

    public List getMasterInfo() {
        List <MasterInfo> hMasterInfoList = null;
        Query query = new Query();
        query.with(new Sort(Sort.Direction.DESC, "isActiveMaster"));
        hMasterInfoList = mongoTemplate.find(query, MasterInfo.class);

        return hMasterInfoList;
    }
}
