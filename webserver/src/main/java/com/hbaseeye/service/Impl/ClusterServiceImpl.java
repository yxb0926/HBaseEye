package com.hbaseeye.service.Impl;

import com.hbaseeye.model.ClusterInfo;
import com.hbaseeye.service.ClusterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.mongo.MongoProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;
import java.util.List;

/**
 * Created by yuanxiaobin on 16/12/8.
 */
@Service
@EnableConfigurationProperties(MongoProperties.class)
public class ClusterServiceImpl implements ClusterService {

    @Autowired
    private MongoTemplate mongoTemplate;

    public List getClusterInfo() {
        List <ClusterInfo> clusterInfoList = null;
        clusterInfoList = mongoTemplate.findAll(ClusterInfo.class);

        return clusterInfoList;
    }
}
