package com.hbaseeye.service.Impl;

import com.hbaseeye.model.TableFiledsMap;
import com.hbaseeye.service.KpiService;
import com.hbaseeye.utils.KpiMaps;
import com.mongodb.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.data.mongodb.core.CollectionCallback;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * Created by yuanxiaobin on 16/12/12.
 */
@Service
public class KpiServiceImpl implements KpiService {

    @Autowired
    private MongoTemplate mongoTemplate;

    public List getKpi(String type, String tag, final String serverName, final Long startTime, final Long endTime) {
        KpiMaps kpiMaps = new KpiMaps();
        Map<String, TableFiledsMap> map = (Map<String, TableFiledsMap>) kpiMaps.typeTableMap.get(type);
        String tableName = map.get(tag).getTableName();
        String filedName = map.get(tag).getFiledName();

        List<DBObject> resutl = mongoTemplate.execute(tableName, new CollectionCallback<List<DBObject>>(){
            public List<DBObject> doInCollection(DBCollection collection) throws MongoException, DataAccessException{
                DBObject queryCondition = new BasicDBObject();
                queryCondition.put("hostname", serverName);
                queryCondition.put("timestamp", new BasicDBObject("$gt",new Long(startTime)));
                queryCondition.put("timestamp", new BasicDBObject("$lt",new Long(endTime)));

                System.out.println(System.currentTimeMillis());
                DBCursor dbCursor = collection.find(queryCondition);
                System.out.println(System.currentTimeMillis());

                while (dbCursor.hasNext()){
                    System.out.println(dbCursor.next());
                }

                dbCursor.close();
                return null;
                //return dbCursor.toArray();
            }
        });


        /**
        for( DBObject dbObject:resutl){
            System.out.println(dbObject.toString());
        }
        */

        return null;
    }

    private List getData(){


        return null;
    }

}
