package com.hbaseeye.service.Impl;

import com.hbaseeye.model.TableFiledsMap;
import com.hbaseeye.service.KpiService;
import com.hbaseeye.utils.DateTime;
import com.hbaseeye.utils.KpiMaps;
import com.mongodb.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.data.mongodb.core.CollectionCallback;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Service
public class KpiServiceImpl implements KpiService {

    @Autowired
    private MongoTemplate mongoTemplate;

    public List getKpi(String type, String tag, final String serverName, final String startTime, final String endTime) {
        KpiMaps kpiMaps = new KpiMaps();
        Map<String, TableFiledsMap> map = (Map<String, TableFiledsMap>) kpiMaps.typeTableMap.get(type);
        String tableName = map.get(tag).getTableName();
        final String filedName = map.get(tag).getFiledName();

        DateTime dateTime = new DateTime();
        final Long starttime = dateTime.getMSTime(startTime);
        final Long endtime   = dateTime.getMSTime(endTime);

        final List list = new ArrayList();
        List<DBObject> resutl = mongoTemplate.execute(tableName, new CollectionCallback<List<DBObject>>(){
            public List<DBObject> doInCollection(DBCollection collection) throws MongoException, DataAccessException{

                DBObject queryCondition = new BasicDBObject();
                queryCondition.put("hostname", serverName);

                BasicDBObject cond = new BasicDBObject();
                cond.put("$gte", starttime);
                cond.put("$lte", endtime);

                queryCondition.put("timestamp",cond);

                // 指定查询哪个字段，不查询哪个字段
                BasicDBObject filedCondition = new BasicDBObject();
                filedCondition.append("_id", 0);
                filedCondition.append(filedName, 1);


                BasicDBList condList = new BasicDBList();
                condList.add(queryCondition);
                condList.add(filedCondition);

                DBCursor dbCursor = collection.find(queryCondition, filedCondition);

                while (dbCursor.hasNext()){
                    list.add(dbCursor.next().get(filedName));
                }

                return list;
            }
        });

        return list;
    }
}
